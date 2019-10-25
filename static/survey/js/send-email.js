$(document).ready(function() {
    $('.send-diagnostic-email').click(function() {
        const subject = encodeURIComponent($(this).data('subject'));
        const body = encodeURIComponent($(this).data('body'));

        window.location.href = "mailto:info@cases.lu?subject=" + subject + "&body=" + body;
    });
});
