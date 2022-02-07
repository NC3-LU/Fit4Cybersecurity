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

    function pieChart(data,ctx){
        new Chart(ctx, {
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
                },
            },
        });
        return Chart
    };

    function radarChart(labels,data_sets,ctx){
        new Chart(ctx, {
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

    fetch("/stats/survey-status-count.json")
    .then(response => response.json())
    .then(result => {
        var ctx = document.getElementById("stats-count").getContext('2d');
        pieChart(result,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/survey-language-count.json")
    .then(response => response.json())
    .then(result => {
        var ctx = document.getElementById("stats-language").getContext('2d');
        pieChart(result,ctx);
    }).catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/survey_per_country.json")
    .then(response => response.json())
    .then(result => {
        var ctx = document.getElementById("stats-countries").getContext('2d');
        pieChart(result,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/survey_per_company_size.json")
    .then(response => response.json())
    .then(result => {
        var ctx = document.getElementById("stats-company").getContext('2d');
        pieChart(result,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/survey_per_company_sector.json")
    .then(response => response.json())
    .then(result => {
        var ctx = document.getElementById("stats-sector").getContext('2d');
        pieChart(result,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/activity-chart.json")
    .then(response => response.json())
    .then(result => {
        $('#surveys-activity').github_graph({
          data: result ,
          texts: ['completed survey','completed surveys']
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    fetch("/stats/answers-per-section.json")
    .then(response => response.json())
    .then(result => {
        let data_sets = [];
        let labels = [];
        let i = 0;
        for (const [key, value] of Object.entries(result)) {
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

        var ctx = document.getElementById("answers-per-section");
        radarChart(labels,data_sets,ctx);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
