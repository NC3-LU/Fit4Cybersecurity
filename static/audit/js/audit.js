$(document).ready(function() {
    $('.go-to-audit').click(function() {
        window.location.replace('/audit/product/' + $(this).data("go-to-audit"));
    });
});
