// var speedCanvas = document.getElementById("speedChart");

// // Chart.defaults.global.defaultFontFamily = "Lato";
// // Chart.defaults.global.defaultFontSize = 18;

// var dataFirst = {
//     label: "Car A - Speed (mph)",
//     data: [0, 59, 75, 20, 20, 55, 40],
//     lineTension: 0,
//     fill: false,
//     borderColor: 'red'
//   };

// var dataSecond = {
//     label: "Car B - Speed (mph)",
//     data: [20, 15, 60, 60, 65, 30, 70],
//     lineTension: 0,
//     fill: false,
//   borderColor: 'blue'
//   };
// var speedData = {
//   labels: ["0s", "10s", "20s", "30s", "40s", "50s", "60s"],
//   datasets: [dataFirst, dataSecond]
// };

// var chartOptions = {
//   legend: {
//     display: true,
//     position: 'top',
//     labels: {
//       boxWidth: 80,
//       fontColor: 'black'
//     }
//   }
// };

// var lineChart = new Chart(speedCanvas, {
//   type: 'line',
//   data: speedData,
//   options: chartOptions
// });


const multiline = document.getElementById('multipleLineChart').getContext('2d');

const mulitline_chart = new Chart(multiline, {
  type: 'line',
  options: {
    responsive: true,
  //   legend: {
  //     display: false
  // },
  // scales: {
  //       yAxes: [{
  //         ticks: {
  //           beginAtZero: true
  //         }
  //       }]
  //     }
  //   },
    scales: {
      xAxes: [ {
        type: 'time',
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Privious 5 Minutes record chart'
        },
        ticks: {
          major: {
            fontStyle: 'bold',
            fontColor: '#FF0000'
          }
        }
      } ],
      yAxes: [ {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Per Vehicle Count'
        }
      } ]
    }
  },
  data: {
    labels: [
      moment(new Date(2021, 11, 1)).format('YYYY-MM-DD'),
      moment(new Date(2021, 11, 2)).format('YYYY-MM-DD'),
      moment(new Date(2021, 11, 3)).format('YYYY-MM-DD'),
      moment(new Date(2021, 11, 4)).format('YYYY-MM-DD'),
      moment(new Date(2021, 11, 5)).format('YYYY-MM-DD'),
      moment(new Date(2021, 11, 6)).format('YYYY-MM-DD')
    ],
    // ["Car", "Bus", 'Truck', "Rickshaw", "Bike", "Van"]
    datasets: [{
      label: 'Car',
      data: [2,4,6,3,2,5],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(255, 99, 132, 0.5)'

      // borderColor: 'red'
    },
    {
      label: 'Bus',
      data: [2,3,4,2,1,2],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(54, 162, 235, 0.5)'

      // borderColor: 'green'
    },
    {
      label: 'truck',
      data: [0,1,2,3,0,0],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(255, 206, 86, 0.5)'

      // borderColor: 'pink'
    }
      ,
    {
      label: 'Rickshaw',
      data: [4,5,6,7,8,9],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(75, 192, 192, 0.5)'

      // borderColor: 'blue'
    },
    {
      label: 'Bike',
      data: [0,0,0,1,2,4],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(153, 102, 255, 0.5)'

      // borderColor: 'black'
    }
      ,
    {
      label: 'van',
      data: [0,1,0,1,0,1],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(255, 159, 64, 0.5)'
      // borderColor: 'yellow'
    }
    ],
  },
  // options: {

  //  
});
// multi line chart end

var index = document.getElementById("indexchart").getContext("2d");
var myChart = new Chart(index, {
  type: 'line',

  options: {
    responsive: true,
    legend: {
      display: false
  },
    scales: {
      xAxes: [ {
        type: 'time',
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Privious 5 Minutes data chart'
        },
        ticks: {
          major: {
            fontStyle: 'bold',
            fontColor: '#FF0000'
          }
        }
      } ],
      yAxes: [ {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Vehicle Count'
        }
      } ]
    }
  },
  // options: {
  //   scales: {
  //     xAxes: [{
  //       type: 'time',
  //     }]
    
  //   }
  //   ,
  //   scales: {
  //     y: {
  //         beginAtZero: true
  //     }
  // }

  // },
  data: {
    // labels: ["2015-03-15T13:03:00Z", "2015-03-25T13:02:00Z", "2015-04-25T14:12:00Z"],
    datasets: [{
      // label: 'Live Data',
      data: [
        {
        't': '2021-11-17:19:08:40',
        'y': 3
      }
      // ,
      // {
      //   't': '2021-10-05 15:51:25.229885',
      //   'y': 10
      // },
      // {
      //   't': '2021-10-05 15:51:20.229885',
      //   'y': 5
      // }
    ]
      ,
      backgroundColor: [
        'rgba(255, 99, 132, 0.4)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }]
  }
  // options: {
    
// }
});

// var index = document.getElementById("indexchart").getContext("2d");
// var myChart = new Chart(index, {
//   type: 'line',
//   options: {
//     scales: {
//       xAxes: [{
//         type: 'time',
//       }]
//     }, scales: {
//       yAxes: [{
//         ticks: {
//           beginAtZero: true
//         }
//       }]
//     }
//     //   scales: {
//     //     y: {
//     //         beginAtZero: true
//     //     }
//     // }

//   },
//   data: {
//     // labels: ["2021-11-9:03:00Z", "2015-03-25T13:02:00Z", "2015-04-25T14:12:00Z"],
//     datasets: [{
//       label:"",
//       data: [
//             { t: new Date("2021-11-8:13:1"), y: 12 },
//             { t: new Date("2021-11-8:13:2"), y: 21 },
//             { t: new Date("2021-11-8:13:3"), y: 32 },
//             { t: new Date("2021-11-8:13:4"), y: 12 },
//             { t: new Date("2021-11-8:13:5"), y: 21 },
//             { t: new Date("2021-11-8:13:6"), y: 32 }
//       ],
//       backgroundColor: [
//         'rgba(255, 99, 132, 0.2)',
//         'rgba(54, 162, 235, 0.2)',
//         'rgba(255, 206, 86, 0.2)',
//         'rgba(75, 192, 192, 0.2)',
//         'rgba(153, 102, 255, 0.2)',
//         'rgba(255, 159, 64, 0.2)'
//       ],
//       borderColor: [
//         'rgba(255,99,132,1)',
//         'rgba(54, 162, 235, 1)',
//         'rgba(255, 206, 86, 1)',
//         'rgba(75, 192, 192, 1)',
//         'rgba(153, 102, 255, 1)',
//         'rgba(255, 159, 64, 1)'
//       ],
//       borderWidth: 1
//     }]
//   },
//   // options: {

//   //   scales: {
//   //     yAxes: [{
//   //     	ticks: {
//   //       	beginAtZero: true
//   //       }
//   //     }]
//   //   }
//   // }
//   // options: {

//   // }
// });

// BAR CHART CHARTJS
var bar = document.getElementById("barchart");
var barChart = new Chart(bar, {
  type: 'bar',
  options:{
    responsive:true,
    legend: {
      display: false
  }
  },
  data: {
    labels: ["Car", "Bus", 'Truck', "Rickshaw", "Bike", "Van"],
    datasets: [{
      label: 'Bar Chart',
      data: [4,1,3,6,3,2],
      backgroundColor: [
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)',
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }]
  }
  // options: {
  //   responsive: true
  // }

});


// BAR Chart end chartjs
var pie = document.getElementById("piechart");
var pieChart = new Chart(pie, {
  type: 'doughnut',
  data: {
    labels: ["Car", "Bus", 'Truck', "Rickshaw", "Bike", "Van"],
    datasets: [{
      // label: 'Bar Chart',
      data: [4,1,3,6,3,2],
      backgroundColor: [
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)',
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }]
  },
  options: {
    responsive: true
  }

});

function labelFormatter(label, series) {
  return '<div style="font-size:13px; text-align:center; padding:2px; color: #fff; font-weight: 600;">'
    + label
    + '<br>'
    + Math.round(series.percent) + '%</div>'
}







const sio = io('http://' + document.domain + ':' + location.port);

sio.on('connect', () => {
  console.log('connected clint js');
  //   sio.emit('sum', {numbers: [1, 2]});
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on("frame", (data) => {
  console.log("frame recieved")
  document.getElementById("frames").src = "data:image/png;base64," + data;

});

sio.on('index data', (data) => {
  // console.log("image data recieved website")
  // console.log(data['indexchart'])
  // console.log(bardata)
  myChart.data.datasets[0].data.push(data['indexchart'])
  pieChart.data.datasets[0].data = data['data']
  barChart.data.datasets[0].data = data['data']

  for (var i = 0; i < data['data'].length; i++) {
    mulitline_chart.data.datasets[i].data.push(data['data'][i])
  }
  mulitline_chart.data.labels.push(data['time'])
  // console.log(data['data'])
  // console.log(barChart.data.datasets.data)
  // console.log(myChart.data.datasets[0].data)
  myChart.update()
  barChart.update()
  pieChart.update()
  mulitline_chart.update()
  if (mulitline_chart.data.labels > 30) {
    for (var i = 0; i < data['data'].length; i++) {
      mulitline_chart.data.datasets[i].data.shift()
    }
    mulitline_chart.data.labels.shift()
    myChart.data.datasets[0].data.shift()
  }
});
sio.on('page load', (data) => {
  console.log(data)
  // console.log("image data recieved website")
  // console.log(data['indexchart'])
  // console.log(bardata)
  myChart.data.datasets[0].data=data['indexchart']
  // pieChart.data.datasets[0].data = data['data']
  // barChart.data.datasets[0].data = data['data']

  for (var i = 0; i < data['multi'].length; i++) {
    mulitline_chart.data.datasets[i].data=data['multi'][i]
  }
  mulitline_chart.data.labels=data['time']
  // console.log(data['data'])
  // console.log(barChart.data.datasets.data)
  // console.log(myChart.data.datasets[0].data)
  myChart.update()
  // barChart.update()
  // pieChart.update()
  mulitline_chart.update()
 
});