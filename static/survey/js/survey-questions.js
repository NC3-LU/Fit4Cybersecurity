$(document).ready(function() {
    
    $('form[action^="/survey/question/1"][action$="/1"] textarea').attr('rows', 1);

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
        if (!window.location.href.includes('survey/start')) {
            e.preventDefault();
            $("#modal-leave-survey").modal();
        }
    });

    $('#redirect-home').click(function() {
        window.location.replace($('.logo-link').attr('href'));
    });

    $('#download-report').click(function(e) {
        $('#cover-spin').show(0);
        e.stopImmediatePropagation();
        e.preventDefault();
        let filename = '';
        fetch($('#download-report').attr('href'))
            .then(resp => {
                const header = resp.headers.get('Content-Disposition');
                const parts = header.split(';');
                filename = parts[1].split('=')[1];

                return resp.blob()
            })
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = filename;
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                $('#cover-spin').hide();
            })
            .catch(() => {
                $('#cover-spin').hide();
                alert('An error occurred.')
            });
    });

    let processCheckboxSelection = function(checkbox) {
        submitButton.attr("disabled", !checkboxesAndRadios.is(":checked"));

        let answerContentTextarea = $('#id_answer_content');
        if (checkbox.is(":checked") && freeTextAnswerId == checkbox.val()) {
            answerContentTextarea.show();
            answerContentTextarea.focus()
            answerContentTextarea.prop('required', true);
        } else if (!checkbox.is(":checked") && freeTextAnswerId == checkbox.val() && checkbox.hasClass('multiple-selection')) {
            answerContentTextarea.hide();
            answerContentTextarea.prop('required', false);
        } else if (checkbox.hasClass('radio-buttons')) {
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

        /* Process answers dependencies. */
        if (checkbox.data('dependant-ids')) {
            var answersDependancies = checkbox.data('dependant-ids');
            jQuery.each(answersDependancies, function(ind, answerDependancy) {
                if (answerDependancy['leadId'] == checkbox.val()) {
                    var dependantIds = answerDependancy['dependantIds'];
                    for (var i = 0; i < dependantIds.length; i++) {
                        checkboxesAndRadios.each(function() {
                            if ($(this).val() == dependantIds[i]) {
                                $(this).prop("disabled", checkbox.is(":checked"));
                                $(this).parent("label").css("color", checkbox.is(":checked") ? "#ccc" : "");
                            }
                        });
                    }
                }
            });
        }
    }

    var checkboxesAndRadios = $(".form-group input[type='checkbox'], input[type='radio']"),
        checkboxes = $(".form-group input[type='checkbox']"),
        submitButton = $(".form-group input[type='submit']");
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
                $(".form-check-label").hide();            
                answerContentTextarea.show();
                answerContentTextarea.prop('required', true);
            }
        });
    }

    var contextQuestions = $('#context_questions').children(".form-group");
    if (contextQuestions) {
        contextQuestions.children(".form-control").removeClass("is-valid");
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

    let isAnswerChanged = false;
    if ($('.radio-buttons.form-check-input').length > 0) {
        let initial_radio_val = $('.radio-buttons.form-check-input:checked').val();
        $('.radio-buttons.form-check-input').change(function() {
            if ($('.radio-buttons.form-check-input:checked').val() != initial_radio_val) {
                isAnswerChanged = true;
            } else {
                isAnswerChanged = false;
            }
        });
    }
    if ($('.multiple-selection.form-check-input').length > 0) {
        let initiallySelectedValues = [];
        $.each($(".multiple-selection.form-check-input:checked"), function() {
            initiallySelectedValues.push($(this).val());
        });
        $('.multiple-selection.form-check-input').change(function() {
            let currentlySelectedValues = [];
            $.each($(".multiple-selection.form-check-input:checked"), function() {
                currentlySelectedValues.push($(this).val());
            });
            isAnswerChanged = currentlySelectedValues.length !== initiallySelectedValues.length ||
                !currentlySelectedValues.every((v, i) => v === initiallySelectedValues[i])
        });
    }

    $('.modify-question').click(function(event) {
        event.preventDefault();
        if (isAnswerChanged) {
            $("#modal-answer-changing-warning").modal();
            $('#submit-form').click(function() {
                $('#survey-question-form').submit();
            })
        } else {
            $('#survey-question-form').submit();
        }
    })
});
