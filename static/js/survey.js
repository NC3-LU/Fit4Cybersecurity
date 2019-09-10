$("#continue-later").on("click", function(event) {
    event.preventDefault();
    $(".popup-overlay, .popup-content").addClass("active");
});

$(".close, .popup").on("click", function() {
    $(".popup, .popup-content").removeClass("active");
});