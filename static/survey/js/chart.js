$(document).ready(function () {

    if (typeof categoriesData !== 'undefined' && typeof categoriesLabels !== 'undefined') {
        let ctx = document.getElementById('chartByCategory');
        radarChart(categoriesLabels,categoriesData,ctx);
    }

    if (typeof sectionsData !== 'undefined' && typeof sectionsLabels !== 'undefined') {
        let ctx = document.getElementById('chartBySections');
        radarChart(sectionsLabels,sectionsData,ctx);
    }

    function radarChart(labels,data_sets,ctx){
        let wrapedLabels = [];
        labels.forEach( label => {wrapedLabels.push(wrapLabel(label))});
        return new Chart(ctx, {
            type: 'radar',
            data: {
                labels: wrapedLabels,
                datasets: [
                    {
                        fill: true,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        pointBackgroundColor: 'rgb(255, 99, 132)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgb(255, 99, 132)',
                        data: data_sets,
                    }
                ]
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
                        display: false,
                    },
                },
            }
        });
    }

    function wrapLabel(label, maxwidth = 15){
        let sections = [];
        let words = label.split(" ");
        let temp = "";

        words.forEach(function(item, index){
            if(temp.length > 0)
            {
                var concat = temp + ' ' + item;

                if(concat.length > maxwidth){
                    sections.push(temp);
                    temp = "";
                }
                else{
                    if(index == (words.length-1))
                    {
                        sections.push(concat);
                        return;
                    }
                    else{
                        temp = concat;
                        return;
                    }
                }
            }

            if(index == (words.length-1))
            {
                sections.push(item);
                return;
            }

            if(item.length < maxwidth) {
                temp = item;
            }
            else {
                sections.push(item);
            }
        });

        return sections;
    }
});
