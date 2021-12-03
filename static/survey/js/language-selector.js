$(document).ready(function() {
    var currentLanguageValue = $("#language-selector a.dropdown-toggle").html().replace(/\r?\n|\s/g, "");
    $("#language-selector .dropdown-item").click(function(event) {
        if ($(this).html().replace(/\r?\n|\s/g, "") == currentLanguageValue) {
            event.preventDefault();
        }
    });
});
