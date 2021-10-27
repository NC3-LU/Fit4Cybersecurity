$(document).ready(function() {
    $("#language-selector .dropdown-item").click(function(){
      $("#language-selector .dropdown-toggle:first-child").html(
        '<span class="flag-icon flag-icon-'
        + $(this).attr('value')
        + '"></span>'
        + $(this).text()
      );
    });
});
