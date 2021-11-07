const sio = io('http://' + document.domain + ':' + location.port);

sio.on('connect', () => {
  console.log('connected clint js');
  //   sio.emit('sum', {numbers: [1, 2]});
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on("frame predict", (data) => {
  console.log("frame recieved")
  document.getElementById("frames").src = "data:image/png;base64," + data;

});

sio.on("page data detection", (data) =>{
    // console.log(data['carcount'])
    // document.getElementById("frames").src = "data:image/png;base64," + json['image'];
    document.getElementById("total").textContent=data['total']
    document.getElementById("carcount").textContent=data['cartotal']
    document.getElementById("buscount").textContent=data['bustotal']
    document.getElementById("truckcount").textContent=data['trucktotal']
    document.getElementById("bikecount").textContent=data['biketotal']
    document.getElementById("rickshawcount").textContent=data['rickshawtotal']
    document.getElementById("vancount").textContent=data['vantotal']
});