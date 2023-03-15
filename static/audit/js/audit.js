var complianceData = {};
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

$(document).ready(function() {
    $('.go-to-edit').click(function() {
        var $popup = $("#editProduct");
        var popup_url = '/audit/edit/' + $(this).data("go-to-edit");
        $(".modal-dialog", $popup).load(popup_url, function () {
          $popup.modal("show");
        });
    });

    $('#statusDetails').on('show.bs.modal', function(e) {
        let auditId = $(e.relatedTarget).data('audit-id');
        let chart = Chart.getChart("complianceStatus");
        if (chart != undefined) chart.destroy();
        let ctx = document.getElementById('complianceStatus');
        pieChart(complianceData[auditId],ctx);
    });

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
});

function onBlurTextarea(form){
    const csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    data = JSON.stringify({"id":form.id, [form.name]:form.value});
    fetch(window.location.pathname, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken
        },
        body: data
      })
      .then()
      .catch((error) => {
        console.log(error);
      });
}

function onChangeSelect(form){
    const csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    data = JSON.stringify({"id":form.id, [form.name]:form.value});
    fetch(window.location.pathname, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken
        },
        body: data
      })
      .then()
      .catch((error) => {
        console.log(error);
      });
}
