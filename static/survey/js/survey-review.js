$(document).ready(function() {

    $('.flag-icon-lb').addClass('flag-icon-lu').removeClass('flag-icon-lb');

    $('.modify-question').click(function() {
        window.location.replace('/survey/question/' + $(this).data("question"));
    });
});
