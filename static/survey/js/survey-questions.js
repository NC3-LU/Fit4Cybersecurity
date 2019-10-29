$(document).ready(function() {

    const download = function(filename, text) {
        const pom = document.createElement('a');
        pom.setAttribute('href', 'data:application/plain;charset=utf-8,' + encodeURIComponent(text));
        pom.setAttribute('download', filename);

        if (document.createEvent) {
            const event = document.createEvent('MouseEvents');
            event.initEvent('click', true, true);
            pom.dispatchEvent(event);
        }
        else {
            pom.click();
        }
    }

    $('#download-direct-link').click(function() {
        const uriContent = '<!DOCTYPE html><head><meta charset="UTF-8"><meta http-equiv="refresh" content="0; url='
            + $('#direct-link').data('link') + '"></head><body></body></html>';
        download('SecuritySurvey.html', uriContent);
    });

    $('#direct-link').on('mouseup', function() {
        $(this).select();
    });

    $('#resume-later-code').on('mouseup', function() {
        $(this).select();
    });

    $('.logo-link').click(function(e) {
        let preventRedirectUris = ['/survey/question', '/survey/finish'];
        if (preventRedirectUris.includes(window.location.pathname)) {
            e.preventDefault();
            $("#modal-leave-survey").modal();
        }
    });

    $('#redirect-home').click(function() {
        window.location.replace('/');
    });

    var checkboxes = $("input[type='checkbox'], input[type='radio']"),
        submitButton = $("input[type='submit']");
    submitButton.attr("disabled", checkboxes.length > 0);

    checkboxes.click(function(element) {
        submitButton.attr("disabled", !checkboxes.is(":checked"));

        $(element).data('is_unique')
    });
});
