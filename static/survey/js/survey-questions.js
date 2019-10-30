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

    var checkboxesAndRadios = $("input[type='checkbox'], input[type='radio']"),
        checkboxes = $("input[type='checkbox']"),
        submitButton = $("input[type='submit']");
    submitButton.attr("disabled", checkboxesAndRadios.length > 0);

    checkboxesAndRadios.click(function() {
        submitButton.attr("disabled", !checkboxesAndRadios.is(":checked"));

        if (checkboxes.length == 0) {
            return;
        }

        let currentCheckbox = $(this);
        let uniqueAnswers = $("input[name=unique_answers]").val().split(',');

        if (uniqueAnswers.length > 0) {
            if (uniqueAnswers.includes(currentCheckbox.val())) {
                checkboxesAndRadios.each(function() {
                    if ($(this).val() != currentCheckbox.val()) {
                        $(this).prop("disabled", currentCheckbox.is(":checked"));
                        $(this).parent("label").css("color", currentCheckbox.is(":checked") ? "#ccc" : "");
                    }
                });
            } else {
                if (currentCheckbox.is(":checked")) {
                    checkboxesAndRadios.each(function() {
                        if (uniqueAnswers.includes($(this).val())) {
                            $(this).prop("disabled", true);
                            $(this).parent("label").css("color", "#ccc");
                        }
                    });
                } else if (!checkboxesAndRadios.is(":checked")) {
                    checkboxesAndRadios.each(function() {
                        if (uniqueAnswers.includes($(this).val())) {
                            $(this).prop("disabled", false);
                            $(this).parent("label").css("color", "");
                        }
                    });
                }
            }
        }
    });
});
