$(document).ready(function () {
    if (typeof chartData !== 'undefined' && typeof chartLabels !== 'undefined') {
        let ctx = document.getElementById('result-chart');
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
                responsive: true,
                maintainAspectRatio: true,
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
                elements: {
                    line: {
                        borderWidth: 3
                    }
                },
                layout: {
                    padding: {
                        left: 65,
                        right: 60
                    }
                }
            }
        });
    }
});
