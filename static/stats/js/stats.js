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
});
document.addEventListener("DOMContentLoaded", function() {
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
                plugins: {
                    legend: {
                        position: 'bottom',
                    },
                },
            },
        });
        return Chart
  };

  fetch("/stats/survey-status-count.json")
  .then(response => response.json())
  .then(result => {
    var ctx = document.getElementById("stats-count").getContext('2d');
    var myChart = pieChart(result,ctx);
    }).catch((error) => {
      console.error('Error:', error);
    });

    fetch("/stats/survey-language-count.json")
    .then(response => response.json())
    .then(result => {
      var ctx = document.getElementById("stats-language").getContext('2d');
      var myChart = pieChart(result,ctx);
      }).catch((error) => {
        console.error('Error:', error);
      });

    fetch("/stats/survey_context.json")
    .then(response => response.json())
    .then(result => {
        var ctx = document.getElementById("stats-company").getContext('2d');
        pieChart(result["company_sizes"],ctx);
        ctx = document.getElementById("stats-countries").getContext('2d');
        pieChart(result["countries"],ctx);
        ctx = document.getElementById("stats-sector").getContext('2d');
        pieChart(result["sectors"],ctx);
    }).catch((error) => {
      console.error('Error:', error);
    });

    fetch("/stats/activity-chart.json")
    .then(response => response.json())
    .then(result => {
        $('#surveys-activity').github_graph( {
          data: result ,
          texts: ['completed survey','completed surveys']
        });
      }).catch((error) => {
        console.error('Error:', error);
      });

    fetch("/stats/answers-per-section.json")
    .then(response => response.json())
    .then(result => {

      var data_sets = [];
      var labels = [];
      var i = 0;
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
          pointHoverBorderColor: 'rgb(255, 99, 132)'
        })
        i++;
      }

      var ctx = document.getElementById("answers-per-section");
      var myChart = new Chart(ctx, {
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
          }
        }
      });
      }).catch((error) => {
        console.error('Error:', error);
      });
});
