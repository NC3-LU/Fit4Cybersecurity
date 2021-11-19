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
        e.preventDefault();
        $("#modal-leave-survey").modal();
    });

    $('#redirect-home').click(function() {
        window.location.replace('/');
    });

    let processCheckboxSelection = function(checkbox) {
        submitButton.attr("disabled", !checkboxesAndRadios.is(":checked"));

        let answerContentTextarea = $('#id_answer_content');
        if (checkbox.is(":checked") && freeTextAnswerId == checkbox.val()) {
            answerContentTextarea.show();
            answerContentTextarea.prop('required', true);
        } else {
            answerContentTextarea.hide();
            answerContentTextarea.prop('required', false);
        }

        if (checkboxes.length == 0) {
            return;
        }

        let uniqueAnswers = $("input[name=unique_answers]").val().split(',');

        if (uniqueAnswers.length > 0) {
            if (uniqueAnswers.includes(checkbox.val())) {
                checkboxesAndRadios.each(function() {
                    if ($(this).val() != checkbox.val()) {
                        $(this).prop("disabled", checkbox.is(":checked"));
                        $(this).parent("label").css("color", checkbox.is(":checked") ? "#ccc" : "");
                    }
                });
            } else {
                if (checkbox.is(":checked")) {
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
    }

    var checkboxesAndRadios = $("input[type='checkbox'], input[type='radio']"),
        checkboxes = $("input[type='checkbox']"),
        submitButton = $("input[type='submit']");
    if (checkboxesAndRadios.length > 0) {
        processCheckboxSelection(checkboxesAndRadios.filter(':checked').first());
    }

    if (checkboxes.length > 0) {
        $(".select-multi-info").show();
    }

    var answerContentTextarea = $('#id_answer_content');
    if (answerContentTextarea) {
        answerContentTextarea.hide();
        answerContentTextarea.prop('required', false);
    }
    var freeTextAnswerId = $('#id_free_text_answer_id').val();
    if (freeTextAnswerId != 0) {
        checkboxesAndRadios.each(function() {
            let element = $(this);
            if (element.is(":checked") && element.val() == freeTextAnswerId) {
                answerContentTextarea.show();
                answerContentTextarea.prop('required', true);
            }
        });
    }

    checkboxesAndRadios.click(function() {
        processCheckboxSelection($(this));
    });

    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    $('.return-to-question').click(function() {
        window.location.replace('/survey/question/' + $(this).data("return-to-question"));
    });

    $('.cancel-modifications').click(function() {
        window.location.replace('/survey/review#question-' + $(this).data('question-index'));
    });

    $('#id_feedback')
        .click(function() {
            $(this).css('height', '120px');
            $(this).css('width', '80%');
        })
        .focusout(function() {
            $(this).css('height', '60px');
            $(this).css('width', 'auto');
        });

    var qrcodes = $('.qrcode');
    if (qrcodes.length > 0) {
        qrcodes.each(function() {
            var qrcode = new QRCode(this, {
                width: 120,
                height: 120,
                useSVG: true
            });
            qrcode.makeCode($('#direct-link').data('link'));
        });
    }
});
