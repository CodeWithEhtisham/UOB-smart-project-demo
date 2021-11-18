#!/usr/bin/python3
from flask import Flask, Response, render_template, request, jsonify
import json
from PIL import Image
import io
import sqlite3
import base64
import numpy as np
import pandas as pd
from flask_socketio import SocketIO,emit
import datetime as dt
from databases import Database
import asyncio
import time
app = Flask(__name__)
sio=SocketIO(app)

def database():
    return Database("sqlite:///database.db")
    
async def insert_something(db: Database,data):
    async with db.connection() as conn:
        async with db.transaction():
            await db.execute("INSERT INTO data(camera_id,camera_loc,capture_time,image_path) VALUES(:camera_id,:camera_loc,:capture_time,:image_path)",data[0])
            # await db.execute("insert into person (name) values (:name)", {"name": "testing..."})
            query = "SELECT * FROM data ORDER BY frame_id DESC LIMIT 1"
            frame_id = await db.fetch_all(query=query)
            # print(frame_id[0][-1])
            frame_id=frame_id[0][-1]
            # print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            # print(frame_id)
            for index,obj in enumerate(data[1]):
                data[1][index]['frame_id']=frame_id
            # # {'label': 'Car', 'prob': '0.94', 'x': '306', 'y': '259', 'w': '27', 'h': '44', 'frame_id': '12345'}
            # print(data[1])
            await db.execute_many("INSERT INTO results(frame_id,label,prob,x,y,w,h) values(:frame_id,:label,:prob,:x,:y,:w,:h)",data[1])
            print("record added successfull")


async def run(data):
    async with database() as db:
        await insert_something(db,data)
async def fetch_record():
    async with database() as db:
        async with db.connection() as conn:
            async with db.transaction():
                print("record fetching")
                # -- SELECT data.capture_time,data.image_path,results.label,data.frame_id from data join results ON data.frame_id=results.frame_id ORDER by data.frame_id desc LIMIT 100; 
                # -- SELECT frame_id,label from results WHERE results.frame_id in (SELECT frame_id from data ORDER by data.frame_id DESC limit 3);
                rows=await db.fetch_all('SELECT data.capture_time,results.label,data.frame_id from data join results ON data.frame_id=results.frame_id ORDER by data.frame_id desc LIMIT 50')
                index={}
                dic={
                "cartotal":0,
                "bustotal":0,
                "trucktotal":0,
                "rickshawtotal":0,
                "biketotal":0,
                "vantotal":0,
                "total":0

                }
                times=[]
                for i in rows:
                    if i[0] not in index.keys():
                        index[i[0]]=[i[1]]
                    else:
                        index[i[0]].append(i[1])
                    times.append(i[0])
                    # print(i[1])
                    if i[1] =='Motorcycle' or i[1]=="Bicycle":
                        dic['biketotal']+=1
                        dic['total']+=1
                    elif i[1]=='Auto_rikshaw':
                        dic['rickshawtotal']+=1
                        dic['total']+=1
                    elif i[1]=='Bus':
                        dic['bustotal']+=1
                        dic['total']+=1
                    elif i[1]=='Truck':
                        dic['trucktotal']+=1
                        dic['total']+=1
                    elif i[1]=='Van':
                        dic['vantotal']+=1
                        dic['total']+=1
                    else:
                        dic['cartotal']+=1
                        dic['total']+=1
                    # print("type :",rows[0])
                    # time.sleep(6)
                    # ROWS=await db.fetch_all("SELECT * from data LEFT JOIN results ON data.frame_id=results.frame_id ORDER by data.frame_id desc limit 100")
                    # print("rows",rows)
                print(index)
                time.sleep(10)
                return {
                    "counts":dic,
                    "datetime":times
                }

# [{'camera_id': '12345', 'camera_loc': 'UOB', 'capture_time': '2021-11-14 23:32:26.713220', 'image_path': '2021-11-14 23:32:26.713220_uob.jpg'}, [{'label': 'Car', 'prob': '0.89', 'x': '213', 'y': '304', 'w': '40', 'h': '47'}, {'label': 'Car', 'prob': '0.88', 'x': '229', 'y': '261', 'w': '33', 'h': '37'}, {'label': 'Car', 'prob': '0.81', 'x': '174', 'y': '258', 'w': '36', 'h': '47'}, {'label': 'Car', 'prob': '0.76', 'x': '338', 'y': '179', 'w': '15', 'h': '14'}, {'label': 'Car', 'prob': '0.72', 'x': '140', 'y': '335', 'w': '58', 'h': '62'}, {'label': 'Car', 'prob': '0.69', 'x': '369', 'y': '178', 'w': '27', 'h': '19'}, {'label': 'Car', 'prob': '0.67', 'x': '465', 'y': '228', 'w': '46', 'h': '25'}, {'label': 'Car', 'prob': '0.62', 'x': '443', 'y': '217', 'w': '47', 'h': '29'}, {'label': 'Car', 'prob': '0.57', 'x': '394', 'y': '193', 'w': '42', 'h': '29'}, {'label': 'Car', 'prob': '0.57', 'x': '420', 'y': '202', 'w': '41', 'h': '27'}, {'label': 'Car', 'prob': '0.47', 'x': '431', 'y': '209', 'w': '49', 'h': '29'}, {'label': 'Car', 'prob': '0.45', 'x': '306', 'y': '158', 'w': '9', 'h': '9'}, {'label': 'Car', 'prob': '0.39', 'x': '227', 'y': '188', 'w': '12', 'h': '13'}, {'label': 'Car', 'prob': '0.39', 'x': '214', 'y': '221', 'w': '26', 'h': '37'}, {'label': 'Car', 'prob': '0.33', 'x': '572', 'y': '285', 'w': '38', 'h': '42'}, {'label': 'Car', 'prob': '0.24', 'x': '155', 'y': '231', 'w': '24', 'h': '30'}, {'label': 'Bus', 'prob': '0.91', 'x': '479', 'y': '282', 'w': '160', 'h': '212'}, {'label': 'Motorcycle', 'prob': '0.82', 'x': '91', 'y': '412', 'w': '32', 'h': '43'}, {'label': 'Motorcycle', 'prob': '0.74', 'x': '141', 'y': '437', 'w': '28', 'h': '52'}, {'label': 'Motorcycle', 'prob': '0.66', 'x': '403', 'y': '284', 'w': '21', 'h': '32'}, {'label': 'Motorcycle', 'prob': '0.37', 'x': '442', 'y': '347', 'w': '25', 'h': '55'}, {'label': 'Motorcycle', 'prob': '0.31', 'x': '162', 'y': '289', 'w': '26', 'h': '35'}, {'label': 'Motorcycle', 'prob': '0.25', 'x': '322', 'y': '220', 'w': '17', 'h': '18'}, {'label': 'Auto_rikshaw', 'prob': '0.79', 'x': '76', 'y': '302', 'w': '60', 'h': '55'}, {'label': 'Auto_rikshaw', 'prob': '0.44', 'x': '45', 'y': '320', 'w': '47', 'h': '67'}, {'label': 'Auto_rikshaw', 'prob': '0.36', 'x': '13', 'y': '341', 'w': '56', 'h': '84'}, {'label': 'Auto_rikshaw', 'prob': '0.26', 'x': '304', 'y': '178', 'w': '18', 'h': '35'}]]
@sio.on("connect")
def connect():
    print("client connected successful")
    

    # d=[{'camera_id': '12345', 'camera_loc': 'UOB', 'capture_time': '2021-11-14 23:32:19.335265', 'image_path': '2021-11-14 23:32:19.335265_uob.jpg'},
    #  [{'label': 'Car', 'prob': '0.89', 'x': '229', 'y': '262', 'w': '32', 'h': '37'},
    #   {'label': 'Car', 'prob': '0.85', 'x': '174', 'y': '257', 'w': '36', 'h': '48'},
    #    {'label': 'Car', 'prob': '0.84', 'x': '212', 'y': '305', 'w': '41', 'h': '47'},
    #     {'label': 'Car', 'prob': '0.76', 'x': '338', 'y': '179', 'w': '15', 'h': '14'},
    #      {'label': 'Car', 'prob': '0.75', 'x': '139', 'y': '335', 'w': '58', 'h': '65'},
    #       {'label': 'Car', 'prob': '0.66', 'x': '465', 'y': '228', 'w': '46', 'h': '25'},
    #        {'label': 'Car', 'prob': '0.66', 'x': '369', 'y': '177', 'w': '27', 'h': '19'},
    #         {'label': 'Car', 'prob': '0.61', 'x': '443', 'y': '217', 'w': '47', 'h': '29'},
    #          {'label': 'Car', 'prob': '0.56', 'x': '214', 'y': '222', 'w': '26', 'h': '34'},
    #           {'label': 'Car', 'prob': '0.56', 'x': '394', 'y': '193', 'w': '42', 'h': '29'},
    #            {'label': 'Car', 'prob': '0.55', 'x': '420', 'y': '202', 'w': '41', 'h': '27'},
    #             {'label': 'Car', 'prob': '0.48', 'x': '458', 'y': '478', 'w': '109', 'h': '97'},
    #              {'label': 'Car', 'prob': '0.46', 'x': '431', 'y': '209', 'w': '49', 'h': '29'},
    #               {'label': 'Car', 'prob': '0.43', 'x': '305', 'y': '158', 'w': '10', 'h': '9'},
    #                {'label': 'Car', 'prob': '0.38', 'x': '227', 'y': '188', 'w': '12', 'h': '13'},
    #                 {'label': 'Car', 'prob': '0.35', 'x': '572', 'y': '285', 'w': '38', 'h': '42'},
    #                  {'label': 'Car', 'prob': '0.20', 'x': '153', 'y': '231', 'w': '24', 'h': '32'},
    #                   {'label': 'Bus', 'prob': '0.89', 'x': '479', 'y': '280', 'w': '160', 'h': '216'},
    #                    {'label': 'Motorcycle', 'prob': '0.84', 'x': '89', 'y': '415', 'w': '34', 'h': '43'},
    #                     {'label': 'Motorcycle', 'prob': '0.67', 'x': '403', 'y': '283', 'w': '20', 'h': '32'},
    #                      {'label': 'Motorcycle', 'prob': '0.62', 'x': '439', 'y': '344', 'w': '26', 'h': '57'},
    #                       {'label': 'Motorcycle', 'prob': '0.51', 'x': '141', 'y': '441', 'w': '29', 'h': '50'},
    #                        {'label': 'Motorcycle', 'prob': '0.23', 'x': '360', 'y': '443', 'w': '35', 'h': '95'},
    #                         {'label': 'Motorcycle', 'prob': '0.22', 'x': '240', 'y': '236', 'w': '11', 'h': '23'},
    #                          {'label': 'Auto_rikshaw', 'prob': '0.75', 'x': '76', 'y': '301', 'w': '60', 'h': '56'},
    #                           {'label': 'Auto_rikshaw', 'prob': '0.40', 'x': '46', 'y': '319', 'w': '45', 'h': '68'},
    #                            {'label': 'Auto_rikshaw', 'prob': '0.23', 'x': '303', 'y': '177', 'w': '18', 'h': '35'},
    #                             {'label': 'Auto_rikshaw', 'prob': '0.23', 'x': '14', 'y': '340', 'w': '53', 'h': '88'}]]
    # asyncio.run(run(d))
    # emit("page data detection",
    # {"total":50},broadcast=True)

    # emit('graph data',data={
    #       't': '2021-10-05 15:55:50.229885',
    #       'y': 30
    #     },bardata="hello")
    # emit("image","sending data server to clint",broadcast=True)
# @sio.on("detection")
# def detection(json):
#     image=json['image']
@sio.on("main page socket")
def vehicle_detection(json):
    asyncio.run(run([{
        "camera_id":json['camera_id'],
        "camera_loc":json['camera_loc'],
        "capture_time":json['datetime'],
        "image_path":json['image_path']
    },json['results']]))
    counts=json['counts']
    # """detection code here and save into database"""
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
# global flags 
flags=False
waiting=True


def fetchDataframe(limit=200):
    con = sqlite3.connect("database.db")
    mycursor = con.cursor()
    
    # code to split it into 2 lists
    # res1, res2 = map(list, zip(*ini_list))
    if limit != 1:
        mycursor.execute(
        "SELECT * from data LEFT JOIN results ON data.frame_id=results.frame_id ORDER by data.frame_id desc limit {}".format(limit))
        result = mycursor.fetchall()
        con.close()
        df = pd.DataFrame({
            "date": [i[2] for i in result],
            "frame_id": [i[4] for i in result],
            "tag":[i[3] for i in result],
            "vehicle": [i[5] for i in result],
            "id": [i[5] for i in result],
            "lable": [i[7] for i in result]})
        # print(result)
        return df
    else:
        mycursor.execute(
            "SELECT * FROM data ORDER BY data.frame_id desc LIMIT {}".format(limit)
        )
        result=mycursor.fetchall()[0]
        tag=result[-2]
        # print(result[-2])
        # print(result)
        mycursor.execute(
            "SELECT * FROM results where results.frame_id={}".format(result[-1])

        )
        result=mycursor.fetchall()
        con.close()
        dic={
            "Car":0,
            "Bus":0,
            "Truck":0,
            "rikshaw":0,
            "Bike":0,
            "Van":0,
            "total":0

        }
        for i in result:
            # print(i[1])
            if i[2] =='Motorcycle' or i[2]=="Bicycle":
                dic['Bike']+=1
                dic['total']+=1
            elif i[2]=='Auto_rikshaw':
                dic['rikshaw']+=1
                dic['total']+=1
            elif i[2]=='Bus':
                dic['Bus']+=1
                dic['total']+=1
            elif i[2]=='Truck':
                dic['Truck']+=1
                dic['total']+=1
            elif i[2]=='Van':
                dic['Van']+=1
                dic['total']+=1
            else:
                dic['Car']+=1
                dic['total']+=1

        return json.dumps(dic),tag
        # return result
    # return df

def data_check(df, name):
    try:
        return df[name]
    except:
        return 0

def bar_data(df):
    df = df.lable.value_counts()
    # print(data_check(df, "Motorcycle"))
    # print(type(data_check(df, "Motorcycle")))
    return [
        [1, data_check(df, 'Car')],
        [2, data_check(df, "Bus")],
        [3, data_check(df, "Motorcycle") + data_check(df, "Bicycle") ],
        [4, data_check(df, "Van")],
        [5, data_check(df, "Truck")],
        [6, data_check(df, "Auto_rikshaw")]
        # [7, data_check(df, "Auto_rikshaw")]
    ]

def donut_data(df):
    df = df.lable.value_counts()
    s = sum(df.values)
    if s == 0:
        s = 1
    return [
        {
            'label': 'Car',
            'data': int((data_check(df, "Car")/s)*100),
            'color': '#3c8dbc'
        },
        {
            'label': 'Bus',
            'data': int((data_check(df, "Bus")/s)*100),
            'color': '#0073b7'
        },
        {
            'label': 'Truck',
            'data': int((data_check(df, "Truck")/s)*100),
            'color': '#737CA1'
        },
        {
            'label': 'Bike',
            'data': int((data_check(df, "Bike")/s)*100) + int((data_check(df, "Bicycle")/s)*100),
            'color': '#6D7B8D'
        },
        # {
        #     'label': 'Cycle',
        #     'data': int((data_check(df, "Bicycle")/s)*100),
        #     'color': '#566D7E'
        # },
        {
            'label': 'Rikshaw',
            'data': int((data_check(df, "Auto_rikshaw")/s)*100),
            'color': '#00c0ef'
        },
        {
            'label': "Van",
            'data': int((data_check(df, "Van")/s)*100),
            'color': '#6D7B8D'
        }

    ]

def line_plot(df):
    dt = df[['date', 'id']].groupby(by='date').count()
    d = pd.DatetimeIndex(dt.index)
    year, month, day, hour, minute, second = [], [], [], [], [], []

    for i in d:
        # Y = i.year
        # M = i.month
        # D = i.day
        # h = i.hour
        # m = i.minute
        # s = i.second
        year.append(i.year)
        month.append(i.month)
        day.append(i.day)
        hour.append(i.hour)
        minute.append(i.minute)
        second.append(i.second)
    value = [int(i) for i in dt.id.values]
    return year, month, day, hour, minute, second, value, len(dt.id.values)

@app.route("/home", methods=['GET', 'POST'])
def home():
    # try:
    #     del streams
    # except UnboundLocalError:
    #     streams=gen(True)
    # flags=False
    # gen(False)
    return render_template("index.html", jsondata=get_json())
@app.route("/index", methods=['GET', 'POST'])
def index():
    # try:
    #     del streams
    # except UnboundLocalError:
    #     streams=gen(True)
    # flags=False
    # gen(False)
    return render_template("index.html", jsondata=get_json())

@app.route('/')
def main():
    print('main manu uploaded.....')
    rows=asyncio.run(fetch_record())

    # print("sleeping....................")
    # print(len(rows))
    # time.sleep(10)
    return render_template("main.html")

# @sio.
# @app.route('/video_feed')
# def video_feed():
    
#     print("hello")
#     print("frame ",gen())
#     # print(Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame'))
#     return Response(gen(True), mimetype='multipart/x-mixed-replace; boundary=frame')
# @app.route('/livestream',methods=['GET','POST'])
# def livestream():
#     streams=gen(True)
#     return render_template("livestream.html")

@app.route("/history",methods=["GET","POST"])
def history():
    print("history loading")
    if request.method=="POST":
        # print("post histoyr")
        print("start datetime",request.form['start'])
        return render_template("history.html",jsondata=get_json())
    else:
        print("get histoyr")
        return render_template("history.html")
        
@app.route("/prediction",methods=["GET","POST"])
def prediction():
    # print("prediction loading")
    if request.method=="POST":
        # print("post prediction")
        # print("start datetime",request.form['start'])
        return render_template("prediction.html",jsondata=get_json())
    else:
        print("get prediction")
        return render_template("prediction.html")

def send_result(response=None, error='', status=200):
    if response is None:
        response = {}
    result = json.dumps({'result': response, 'error': error})
    return Response(status=status, mimetype="application/json", response=result)
@app.route('/fetchtable',methods=["POST","GET"])
def get_table_data():

    global waiting
    # waiting=False
    while True:
        # print("************************************************** ({})".format(waiting))
        if waiting==True:
            # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ({})".format(waiting))
            break
    df,tag=fetchDataframe(1)
    print(df,tag)
    return df

@app.route('/fetchdata', methods=["POST"])
def get_json():
    # print("hello")
    global flags
    global waiting
    # waiting=False
    while True:
        # print("************************************************** ({})".format(waiting))
        if waiting==True:
            # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ({})".format(waiting))
            break
    if flags == False:
        # print ("flag false statement")
        df = fetchDataframe()
        bar = bar_data(df)
        donut = donut_data(df)
        # print(line_plot(df))
        year, month, day, hour, minute, second, index, ln = line_plot(df)
        flags=True
        return jsonify({
            "bar_data": str(bar),
            "donut_data": donut,
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
            "minute": minute,
            "second": second,
            "line_index_data": index,
            'count': str(np.random.random(1)),
            "checkflag":False
        })
    else:
        # print ("flag true statement")
        df = fetchDataframe()
        bar = bar_data(df)
        donut = donut_data(df)
        # print(line_plot(df))
        year, month, day, hour, minute, second, index, ln = line_plot(df)
        return jsonify({
            "bar_data": str(bar),
            "donut_data": donut,
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
            "minute": minute,
            "second": second,
            "line_index_data": index,
            'count': str(np.random.random(1)),
            "checkflag":True
        })

def db_data_insertion(data):
    try:
        con = sqlite3.connect("database.db")
        sql = "INSERT INTO data(camera_id,camera_loc,capture_time,image_path) VALUES(?,?,?,?)"
        cur = con.cursor()
        cur.execute(sql, data)
        con.commit()
        # print("insertion seccessfull in data table")
        a = cur.lastrowid
        con.close()
        return a
    except Exception as e:
        print("insertion in data table failed :{}".format(e))

def db_results_insertion(data):
    try:
        con = sqlite3.connect("database.db")
        sql = "INSERT INTO results(frame_id,label,prob,x,y,w,h) VALUES(?,?,?,?,?,?,?)"
        cur = con.cursor()
        cur.execute(sql, data)
        con.commit()
        # print("insertiion seccessfull in results table")
        con.close()
    except Exception as e:
        print("insertion in result table failed :{}".format(e))

@app.route("/upload", methods=['POST'])
def login():
    
    global waiting
    waiting=False
    # print("/////////////////////////////////////////////////////////// ({})".format(waiting))
    if request.method == 'POST':
        try:
            img_str = request.json['image']
            tag = request.json["tag"]
            camera_id = request.json['camera_id']
            camera_loc = request.json['camera_loc']
            date_time=request.json["datetime"]
            results = request.json['results']
            img_byte=base64.b64decode(img_str.encode('utf-8'))
            img=Image.open(io.BytesIO(img_byte))
            img.save(f"static/img/output.jpg")
            # img.save(f"static/img/{tag}.jpg")
            # jpg_original = base64.b64decode(img_str)
            # jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
            # img = imdecode(jpg_as_np, flags=1)
            frame_id = db_data_insertion(
                (camera_id, camera_loc,date_time , tag))
            # imwrite(f"static/img/output.jpg", img)

            for r in results:
                lbl = r['label']
                prob = r['prob']
                x = r['x']
                y = r['y']
                w = r['w']
                h = r['h']
                db_results_insertion((frame_id, lbl, prob, x, y, w, h))
            waiting=True
            # print("/////////////////////////////////////////////////////////// ({})".format(waiting))


            return send_result("Frame inserted success", status=201)
        except KeyError as e:
            return send_result(error=f'An "image" file is required {e}', status=422)
        except Exception as e:
            return send_result(error=f'Error {e}', status=500)


if __name__ == "__main__":
    # app.run(host="127.0.0.1",threaded=True)
    app.run(host="192.168.18.34",port=8000,threaded=True,debug=True) # home desktop
