$(document).ready(function() {
    let languageSelector = $("#language-selector a.dropdown-toggle").html();
    if (languageSelector) {
        var currentLanguageValue = languageSelector.replace(/\r?\n|\s/g, "");
        $("#language-selector .dropdown-item").click(function(event) {
            if ($(this).html().replace(/\r?\n|\s/g, "") == currentLanguageValue) {
                event.preventDefault();
            }
        });
    }
});
