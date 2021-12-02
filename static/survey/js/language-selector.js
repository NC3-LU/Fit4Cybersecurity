$(document).ready(function() {
    var target = $(this);
    $("#language-selector .dropdown-item").click(function(){
      $("#language-selector .dropdown-toggle:first-child").html(
        '<span class="flag-icon flag-icon-'
        + $.find(target).attr('value')
        + '"></span>'
        + $.find(target).text()
      );
    });
});
