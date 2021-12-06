#!/usr/bin/python3
from flask import Flask, Response, render_template, request
import json
import base64
from cv2 import imdecode, imwrite
import numpy as np
from flask_socketio import SocketIO,emit
import os
from datetime import datetime
from databases import Database
import eventlet
import asyncio
eventlet.monkey_patch()
app = Flask(__name__)
sio=SocketIO(app)
start_time,end_time=datetime.strftime(datetime.now(), "%Y-%m-%d:%H:%M:%S"),datetime.strftime(datetime.now(), "%Y-%m-%d:%H:%M:%S")

def database():
    return Database("sqlite:///database.db")
    
async def insert_something(db: Database,data):
    async with db.connection() as conn:
        async with db.transaction():
            await db.execute("INSERT INTO data(camera_id,camera_loc,capture_time,image_path) VALUES(:camera_id,:camera_loc,:capture_time,:image_path)",data[0])
            query = "SELECT * FROM data ORDER BY frame_id DESC LIMIT 1"
            frame_id = await db.fetch_all(query=query)
            frame_id=frame_id[0][-1]
            for index,obj in enumerate(data[1]):
                data[1][index]['frame_id']=frame_id
            await db.execute_many("INSERT INTO results(frame_id,label,prob,x,y,w,h) values(:frame_id,:label,:prob,:x,:y,:w,:h)",data[1])
            # print("record added successfull")

async def run(data):
    async with database() as db:
        await insert_something(db,data)

async def fetch_record(status=True,start=None,end=None):
    async with database() as db:
        async with db.connection() as conn:
            async with db.transaction():
                if status:
                    rows=await db.fetch_all('SELECT data.capture_time,results.label,data.frame_id from data join results ON data.frame_id=results.frame_id ORDER by data.frame_id desc LIMIT 500')
                    rows.reverse()
                    index={}
                    for i in rows:
                        if i[0] not in index.keys():
                            index[i[0]]=[i[1]]
                        else:
                            index[i[0]].append(i[1])
                    index_data=[]
                    times=list(index.keys())
                    count=[[],[],[],[],[],[]]
                    for i,j in index.items():
                        index_data.append({
                            't':i,
                            'y':len(j)
                        })
                        car=0
                        bus=0
                        truck=0
                        bike=0
                        van=0
                        rickshaw=0
                        for k in j:
                            if k =='Motorcycle' or k=="Bicycle":
                                bike+=1
                                # dic['total']+=1
                            elif k=='Auto_rikshaw':
                                rickshaw+=1
                                # dic['rickshawtotal']+=1
                                # dic['total']+=1
                            elif k=='Bus':
                                bus+=1
                                # dic['total']+=1
                            elif k=='Truck':
                                truck+=1
                                # dic['total']+=1
                            elif k=='Van':
                                van+=1
                                # dic['total']+=1
                            else:
                                car+=1
                                # dic['total']+=1
                        count[0].append(car)
                        count[1].append(bus)
                        count[2].append(truck)
                        count[3].append(rickshaw)
                        count[4].append(bike)
                        count[5].append(van)                
                        
                    sio.emit('page load',{
                        'indexchart':index_data,
                        "time":times,
                        "multi":count
                        },broadcast=True)
                else:
                    rows=await db.fetch_all(f"SELECT data.capture_time,results.label,data.frame_id from data join results on data.frame_id=results.frame_id  where data.frame_id in (SELECT frame_id from data WHERE capture_time BETWEEN '{start}' AND '{end}')")

                    index={}
                    for i in rows:
                        if i[0] not in index.keys():
                            index[i[0]]=[i[1]]
                        else:
                            index[i[0]].append(i[1])
                    index_data=[]
                    times=list(index.keys())
                    count=[[],[],[],[],[],[]]
                    for i,j in index.items():
                        index_data.append({
                            't':i,
                            'y':len(j)
                        })
                        car=0
                        bus=0
                        truck=0
                        bike=0
                        van=0
                        rickshaw=0
                        for k in j:
                            if k =='Motorcycle' or k=="Bicycle":
                                bike+=1
                                # dic['total']+=1
                            elif k=='Auto_rikshaw':
                                rickshaw+=1
                                # dic['rickshawtotal']+=1
                                # dic['total']+=1
                            elif k=='Bus':
                                bus+=1
                                # dic['total']+=1
                            elif k=='Truck':
                                truck+=1
                                # dic['total']+=1
                            elif k=='Van':
                                van+=1
                                # dic['total']+=1
                            else:
                                car+=1
                                # dic['total']+=1
                        count[0].append(car)
                        count[1].append(bus)
                        count[2].append(truck)
                        count[3].append(rickshaw)
                        count[4].append(bike)
                        count[5].append(van)                
                        
                    sio.emit('page load',{
                        'indexchart':index_data,
                        "time":times,
                        "multi":count
                        },broadcast=True)

async def save_image(filename,image):
    times,area=filename.split('_')
    times=datetime.strftime(datetime.strptime(times, "%Y-%m-%d:%H:%M:%S"), "%Y-%m-%d-%H-%M-%S")
    image=base64.b64decode(image)
    jpg_as_np = np.frombuffer(image, dtype=np.uint8)
    image_buffer = imdecode(jpg_as_np, flags=1)
    # print(f"static//detection images//{times}_{area}")
    imwrite(f"static/detection images/{times}_{area}",image_buffer)


@sio.on("connect")
def connect():
    print("client connected successful")

@sio.on('fetch main page data')
def fetch_main_page_data():
    asyncio.run(fetch_record())

@sio.on("main page socket")
def vehicle_detection(json):
    asyncio.run(run([{
        "camera_id":json['camera_id'],
        "camera_loc":json['camera_loc'],
        "capture_time":json['datetime'],
        "image_path":json['image_path']
    },json['results']]))
    counts=json['counts']
    print("send image data")
    asyncio.run(save_image(json['image_path'],json['image']))
    sio.emit('page data detection',counts,broadcast=True)
    sio.emit('frame predict',json['image'],broadcast=True)
    sio.emit('index data',data={'indexchart':{
                't':json['datetime'],
                'y':counts['total']
            },
            'data':[counts['cartotal'],counts['bustotal'],counts['trucktotal'],counts['rickshawtotal'],counts['biketotal'],counts['vantotal']],
            'time':json['datetime']
            },broadcast=True)

@sio.on("frame get")
def frames(data):
    sio.emit("frame",data,broadcast=True)

@sio.on('my image')
def get_image(image):
    # print(image)
    emit('frame', image,broadcast=True)

@app.route('/history_search',methods=['POST'])
def history_search():
    global start_time
    global end_time
    start_time=datetime.strftime(datetime.strptime(request.form['start'], "%Y-%m-%dT%H:%M"), "%Y-%m-%d:%H:%M:%S") 
    end_time = datetime.strftime(datetime.strptime(request.form['end'], "%Y-%m-%dT%H:%M"), "%Y-%m-%d:%H:%M:%S") 
    asyncio.run(fetch_record(status=False, start=start_time, end=end_time))
    return ('', 204)

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("index.html")
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
@app.route('/')
def main():
    return render_template("main.html")
@app.route("/history",methods=["GET","POST"])
def history():
    return render_template("history.html")    
        
@app.route("/prediction",methods=["GET","POST"])
def prediction():
        return render_template("prediction.html")

def send_result(response=None, error='', status=200):
    if response is None:
        response = {}
    result = json.dumps({'result': response, 'error': error})
    return Response(status=status, mimetype="application/json", response=result)

@app.route('/history_picture',methods=["POST","GET"])
def history_picture():
    global start_time
    global end_time
    list_images=[]
    start=datetime.strftime(datetime.strptime(start_time, "%Y-%m-%d:%H:%M:%S"), "%Y-%m-%d-%H-%M-%S")
    end=datetime.strftime(datetime.strptime(end_time, "%Y-%m-%d:%H:%M:%S"), "%Y-%m-%d-%H-%M-%S")
    for i in os.listdir(r"static/detection images"):
        if start<=i.split('_')[0]<=end:
            list_images.append(i)
    return render_template("gellary.html",images=list_images)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,threaded=True,debug=True) # home desktop
