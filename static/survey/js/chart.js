$(document).ready(function() {
    var ctx = document.getElementById('resultChart');
    var resultChart = new Chart(ctx, {
      type: 'radar',
      data: {
        labels: chartLabels,
        datasets: [
        {
          label: chartTitle,
          fill: true,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          pointBackgroundColor: 'rgb(255, 99, 132)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgb(255, 99, 132)',
          data: chartData,
        }
        ]
      },
      options: {
        scales: {
          r: {
            beginAtZero: true,
            min: 0,
            max: 100,
          }
        },
        elements:{
          line:{
            tension: 0,
            borderWidth: 3
          }
        },
        title: {
          display: false,
        },
        layout: {
          padding: {
            left: 5,
            right: 5,
            top: 5,
            bottom: 5
          }
        }
      }
    });
});
