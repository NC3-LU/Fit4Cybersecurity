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
