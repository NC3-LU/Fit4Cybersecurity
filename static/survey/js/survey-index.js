$(document).ready(function() {
    const updateButtonState = function(button) {
        if (button.val() === '') {
            $('#resume-code-submit').prop('disabled', true);
        } else {
            $('#resume-code-submit').prop('disabled', false);
        }
    }

    $('#resume-code-input').on('change', function () {
        updateButtonState($(this));
    });

    $('#resume-code-input').on('keyup', function () {
        updateButtonState($(this));
    });

    $('#resume-code-submit').on('click', function() {
        let resumeCode = $('#resume-code-input').val();

        if (resumeCode !== '') {
            window.location.replace($('#resume-code-input').data('link') + '?user_id=' + resumeCode);
        }
    });
});
