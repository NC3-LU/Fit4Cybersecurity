$(document).ready(function() {
    $('.modify-question').click(function() {
        window.location.replace('/survey/question/' + $(this).data("question"));
    });
});
