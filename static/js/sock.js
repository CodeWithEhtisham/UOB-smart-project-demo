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
  data: {
    labels: [
      // moment(new Date(2020, 2, 1)).format('YYYY-MM-DD'),
      // moment(new Date(2020, 2, 2)).format('YYYY-MM-DD'),
      // moment(new Date(2020, 2, 3)).format('YYYY-MM-DD')
    ],
    // ["Car", "Bus", 'Truck', "Rickshaw", "Bike", "Van"]
    datasets: [{
        label: 'Car',
        data: [],
        borderWidth: 1,
        fill: false,
        borderColor: 'red'
      },
      {
        label: 'Bus',
        data: [],
        borderWidth: 1,
        fill: false,
        borderColor: 'green'
      },
      {
        label: 'truck',
        data: [],
        borderWidth: 1,
        fill: false,
        borderColor: 'pink'
      }
      ,
      {
        label: 'Rickshaw',
        data: [],
        borderWidth: 1,
        fill: false,
        borderColor: 'blue'
      },
      {
        label: 'Bike',
        data: [],
        borderWidth: 1,
        fill: false,
        borderColor: 'black'
      }
      ,
      {
        label: 'van',
        data: [],
        borderWidth: 1,
        fill: false,
        borderColor: 'yellow'
      }
    ]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});
// multi line chart end


var index = document.getElementById("indexchart").getContext("2d");
var myChart = new Chart(index, {
  type: 'line',
  options: {
    scales: {
      xAxes: [{
        type: 'time',
      }]
    }
  //   scales: {
  //     y: {
  //         beginAtZero: true
  //     }
  // }

  },
  data: {
    // labels: ["2015-03-15T13:03:00Z", "2015-03-25T13:02:00Z", "2015-04-25T14:12:00Z"],
    datasets: [{
      label: 'Live Data',
      data: [
        {
        't': '2021-10-05 15:51:45.229885',
        'y': 20
      },
      {
        't': '2021-10-05 15:51:25.229885',
        'y': 10
      },
      {
        't': '2021-10-05 15:51:20.229885',
        'y': 5
      }
    ]
      ,
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
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

// BAR CHART CHARTJS
var bar = document.getElementById("barchart");
var barChart = new Chart(bar, {
  type: 'bar',
  data: {
    labels: ["Car", "Bus", 'Truck', "Rickshaw", "Bike", "Van"],
    datasets: [{
      label: 'Bar Chart',
      data: [12, 19, 3, 5, 3, 3],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
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
      data: [12, 19, 3, 5, 3, 3],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
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
  pieChart.data.datasets[0].data=data['data']
  barChart.data.datasets[0].data=data['data']

  for (var i = 0; i < data['data'].length; i++) {
    mulitline_chart.data.datasets[i].data.push(data['data'][i])
  }
  mulitline_chart.labels.push(data['time'])
  // console.log(data['data'])
  // console.log(barChart.data.datasets.data)
  // console.log(myChart.data.datasets[0].data)
  myChart.update()
  barChart.update()
  pieChart.update()
  mulitline_chart.update()
});