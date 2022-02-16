$(document).ready(function() {
    $('#save-as-json').click(function() {
        const surveyUsersResults = $('#surveys_users_results').val();
        const pom = document.createElement('a');
        pom.setAttribute('href', 'data:application/json;charset=utf-8,' + encodeURIComponent(surveyUsersResults));
        pom.setAttribute('download', 'survey_results(' + new Date(Date.now()).toLocaleString() + ').json');

        if (document.createEvent) {
            const event = document.createEvent('MouseEvents');
            event.initEvent('click', true, true);
            pom.dispatchEvent(event);
        }
        else {
            pom.click();
        }

        return false;
    });
    $(".dates-limit-form").submit(function(event) {
        $("#surveys_users_results").val('');
    });

    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    if (urlParams.has('from')) {
      var date_from = urlParams.get('from');
    } else {
      var date_from = '';
    }

    if (urlParams.has('to')) {
      var date_to = urlParams.get('to');
    } else {
      var date_to = '';
    }

    var colors = ['rgba(230, 25, 75, 0.4)', 'rgba(60, 180, 75, 0.4)',
        'rgba(255, 225, 25, 0.4)', 'rgba(0, 130, 200, 0.4)', 'rgba(245, 130, 48, 0.4)',
        'rgba(145, 30, 180, 0.4)', 'rgba(70, 240, 240, 0.4)', 'rgba(240, 50, 230, 0.4)',
        'rgba(210, 245, 60, 0.4)', 'rgba(250, 190, 190, 0.4)', 'rgba(0, 128, 128, 0.4)',
        'rgb(148, 163, 209, 0.4)', 'rgba(170, 110, 40, 0.4)', 'rgb(141, 140, 255, 0.4)',
        'rgba(128, 0, 0, 0.4)', 'rgba(170, 255, 195, 0.4)', 'rgba(128, 128, 0, 0.4)',
        'rgba(255, 215, 180, 0.4)', 'rgba(0, 0, 128, 0.4)', 'rgb(241, 147, 241, 0.4)',
        'rgba(255, 255, 255, 0.4)', 'rgb(129, 181, 255, 0.4)', 'rgb(229, 236, 202, 0.4)',
        'rgb(157, 196, 241, 0.4)', 'rgb(253, 141, 211, 0.4)', 'rgb(180, 128, 253, 0.4)',
        'rgb(255, 195, 129, 0.4)', 'rgb(204, 228, 230, 0.4)'];

    var sectionChart = {
        canvas: undefined,
        data: [],
    };

    var categoryChart = {
        canvas: undefined,
        data: [],
    };

    var countryChart = {
        canvas: undefined,
        data: [],
    };

    let section_displayTimeFrame = document.getElementById("section_displayTimeFrame");
    section_displayTimeFrame.onchange = function(event) {
      window.location = "/stats/?from=" + section_displayTimeFrame.value;
    }

    let section_displayByCountry = document.getElementById("section_displayByCountry");
    let category_displayByCountry = document.getElementById("category_displayByCountry");
    section_displayByCountry.onchange = function() {
        let data_sets = [];
        let i = 0;
        for (const [key, value] of Object.entries(sectionChart.data[section_displayByCountry.value])) {
            data_sets.push({
                label: key,
                data: Object.values(value),
                fill: false,
                backgroundColor: colors[i],
                borderColor: colors[i],
                pointBackgroundColor: colors[i],
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: colors[i]
            })
            i++;
        }
        sectionChart.canvas.config.data.datasets = data_sets;
        sectionChart.canvas.update()
    }

    category_displayByCountry.onchange = function() {
        let data_sets = [];
        let i = 0;
        for (const [key, value] of Object.entries(categoryChart.data[category_displayByCountry.value])) {
            data_sets.push({
                label: key,
                data: Object.values(value),
                fill: false,
                backgroundColor: colors[i],
                borderColor: colors[i],
                pointBackgroundColor: colors[i],
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: colors[i]
            })
            i++;
        }
        categoryChart.canvas.config.data.datasets = data_sets;
        categoryChart.canvas.update()
    }


    function pieChart(data,ctx){
        return new Chart(ctx, {
            plugins: [ChartDataLabels],
            type: 'pie',
            data: {
                labels: Object.keys(data),
                datasets: [{
                    data: Object.values(data),
                    borderWidth: 1,
                    backgroundColor: colors
                }],
            },
            options: {
                responsive: true,
                aspectRatio: 0.7,
                plugins: {
                    legend: {
                        position: 'bottom',
                    },
                    datalabels: {
                        formatter: (value, ctx) => {
                            let sum = 0;
                            let dataArr = ctx.chart.data.datasets[0].data;
                            dataArr.map(data => {
                                sum += data;
                            });
                            let percentage = (value*100 / sum).toFixed(0)+"%";
                            return percentage;
                        },
                        anchor: 'end',
                        align: 'start',
                        offset: 5,
                        display: 'auto',
                        color: 'rgba(0,0,0,.7)',
                    }
                },
            },
        });
    };

    $("#stats-countries").click(
        function(evt){
            evt.preventDefault();
            let $popup = $("#popup");
            let activePoints = countryChart.canvas.getElementsAtEventForMode(evt, 'point', countryChart.canvas.options);
            let label = countryChart.canvas.data.labels[activePoints[0].index];
            if (label == others_translation) {
                if (Chart.getChart("stats-countries-detail") == undefined) {
                    let ctx = document.getElementById("stats-countries-detail").getContext('2d');
                    let result = countryChart.data[others_translation]
                    pieChart(result,ctx);
                }else {
                    Chart.getChart("stats-countries-detail").update();
                }
                $popup.modal("show");
            }
        }
    );

    function radarChart(labels,data_sets,ctx){
        return new Chart(ctx, {
            type: 'radar',
            data: {
                labels: labels,
                datasets: data_sets
            },
            options: {
                scale: {
                    min: 0,
                    max: 100,
                },
                elements: {
                    line: {
                        borderWidth: 3
                    }
                },
                plugins: {
                    legend: {
                        position: 'bottom',
                    },
                },
            }
        });
    }

    fetch("/stats/survey-status-count.json?from="+date_from+"&to="+date_to)
    .then(response => response.json())
    .then(result => {
        document.getElementById("spinner-stats-count").innerHTML = "";
        var ctx = document.getElementById("stats-count").getContext('2d');
        var statusChart = pieChart(result,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/survey-language-count.json?from="+date_from+"&to="+date_to)
    .then(response => response.json())
    .then(result => {
        document.getElementById("spinner-stats-language").innerHTML = "";
        var ctx = document.getElementById("stats-language").getContext('2d');
        pieChart(result,ctx);
    }).catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/survey_per_country.json?from="+date_from+"&to="+date_to)
    .then(response => response.json())
    .then(result => {
        countryChart.data = {...result};
        if (result[others_translation]) {
            result[others_translation] = Object.values(result[others_translation]).reduce((a, b) => a + b);
        }
        document.getElementById("spinner-stats-countries").innerHTML = "";
        var ctx = document.getElementById("stats-countries").getContext('2d');
        countryChart.canvas = pieChart(result,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/survey_per_company_size.json?from="+date_from+"&to="+date_to)
    .then(response => response.json())
    .then(result => {
        document.getElementById("spinner-stats-company").innerHTML = "";
        var ctx = document.getElementById("stats-company").getContext('2d');
        var sizeChart = pieChart(result,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/survey_per_company_sector.json?from="+date_from+"&to="+date_to)
    .then(response => response.json())
    .then(result => {
        document.getElementById("spinner-stats-sector").innerHTML = "";
        var ctx = document.getElementById("stats-sector").getContext('2d');
        var sectorChart = pieChart(result,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/activity-chart.json")
    .then(response => response.json())
    .then(result => {
        document.getElementById("spinner-surveys-activity").innerHTML = "";
        $('#surveys-activity').github_graph({
          data: result ,
          texts: ['completed survey','completed surveys'],
          click: function(date, count) {
            window.location = "/stats/?from=" + date;
          }
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/answers-per-section.json?from="+date_from+"&to="+date_to)
    .then(response => response.json())
    .then(result => {
        let data_sets = [];
        let labels = [];
        let i = 0;
        for (const [key, value] of Object.entries(result.all)) {
            labels = Object.keys(value);
            data_sets.push({
                label: key,
                data: Object.values(value),
                fill: false,
                backgroundColor: colors[i],
                borderColor: colors[i],
                pointBackgroundColor: colors[i],
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: colors[i]
            })
            i++;
        }
        sectionChart.data = result;
        document.getElementById("spinner-answers-per-section").innerHTML = "";
        document.getElementById("select-section-displayByCountry").style.display = "block";
        var ctx = document.getElementById("answers-per-section");
        sectionChart.canvas = radarChart(labels,data_sets,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/answers-per-category.json?from="+date_from+"&to="+date_to)
    .then(response => response.json())
    .then(result => {
        let data_sets = [];
        let labels = [];
        let i = 0;
        for (const [key, value] of Object.entries(result.all)) {
            labels = Object.keys(value);
            data_sets.push({
                label: key,
                data: Object.values(value),
                fill: false,
                backgroundColor: colors[i],
                borderColor: colors[i],
                pointBackgroundColor: colors[i],
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: colors[i]
            })
            i++;
        }
        categoryChart.data = result;
        document.getElementById("spinner-answers-per-category").innerHTML = "";
        document.getElementById("select-category-displayByCountry").style.display = "block";
        var ctx = document.getElementById("answers-per-category");
        categoryChart.canvas = radarChart(labels,data_sets,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
