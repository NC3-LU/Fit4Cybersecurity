$(document).ready(function() {
    let ctx = document.getElementById('resultChart');
    let resultChart = new Chart(ctx, {
      type: 'radar',
      data: {
        labels: chartLabels,
        datasets: [
        {
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
        plugins: {
            legend: {
                display: false,
            }
        },
        scales: {
          r: {
            beginAtZero: true,
            min: 0,
            max: 100,
          }
        },
        elements:{
          line:{
            borderWidth: 3
          }
        },
      }
    });
});
