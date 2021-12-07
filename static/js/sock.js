
const multiline = document.getElementById('multipleLineChart');

const mulitline_chart = new Chart(multiline, {
  type: 'line',
  options: {
    responsive: true,

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
    ],
    // ["Car", "Bus", 'Truck', "Rickshaw", "Bike", "Van"]
    datasets: [{
      label: 'Car',
      data: [],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(255, 99, 132, 0.5)'

      // borderColor: 'red'
    },
    {
      label: 'Bus',
      data: [],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(54, 162, 235, 0.5)'

      // borderColor: 'green'
    },
    {
      label: 'truck',
      data: [],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(255, 206, 86, 0.5)'

      // borderColor: 'pink'
    }
      ,
    {
      label: 'Rickshaw',
      data: [],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(75, 192, 192, 0.5)'

      // borderColor: 'blue'
    },
    {
      label: 'Bike',
      data: [],
      borderWidth: 1,
      fill: false,
      borderColor: 'rgba(153, 102, 255, 0.5)'

      // borderColor: 'black'
    }
      ,
    {
      label: 'van',
      data: [],
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

var index = document.getElementById("indexchart");
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

  data: {
    // labels: ["2015-03-15T13:03:00Z", "2015-03-25T13:02:00Z", "2015-04-25T14:12:00Z"],
    datasets: [{
      // label: 'Live Data',
      data: [
        
      // ,
      // {
      //   't': '2021-10-05 15:51:25.229885',
      //   'y': 10
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
    sio.emit('fetch main page data');
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on("frame", (data) => {
  console.log("frame recieved")
  document.getElementById("frames").src = "data:image/png;base64," + data;

});

sio.on('index data', (data) => {
  myChart.data.datasets[0].data.push(data['indexchart'])
  pieChart.data.datasets[0].data = data['data']
  barChart.data.datasets[0].data = data['data']

  for (var i = 0; i < data['data'].length; i++) {
    mulitline_chart.data.datasets[i].data.push(data['data'][i])
  }
  mulitline_chart.data.labels.push(data['time'])
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
  console.log("data recieved 200")
  console.log(data)
  myChart.data.datasets[0].data=data['indexchart']

  for (var i = 0; i < data['multi'].length; i++) {
    mulitline_chart.data.datasets[i].data=data['multi'][i]
  }
  mulitline_chart.data.labels=data['time']
  myChart.update()
  mulitline_chart.update()
 
});

sio.on('history load', (data) => {
  console.log("data recieved 200")
  console.log(data)
  myChart.data.datasets[0].data=data['indexchart']

  for (var i = 0; i < data['multi'].length; i++) {
    mulitline_chart.data.datasets[i].data=data['multi'][i]
  }
  mulitline_chart.data.labels=data['time']
  myChart.update()
  mulitline_chart.update()
 
});