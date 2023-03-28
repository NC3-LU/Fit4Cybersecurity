document.addEventListener("DOMContentLoaded", function () {
    let keyValue = document.cookie.match('(^|;) ?cookiebanner=([^;]*)(;|$)');
    let cookiebannerCookie = keyValue ? decodeURIComponent(keyValue[2]) : null;
    if (cookiebannerCookie) return;

    $('#cookiebannerModal').modal({
        backdrop: 'static',
        keyboard: false
    });
    $(".cookiebannerSubmit").click(function (e) {
        let enable_cookies;
        if (this.name === 'enable_all') {
        enable_cookies = cookiegroups.map((x) => x.id);
        } else {
        let serialized_form = $("#cookiebannerForm").serializeArray();
        let checked_cookiegroups = serialized_form.map((x) => x.name);
        enable_cookies = cookiegroups
                .filter((x) => {
                    return checked_cookiegroups.includes(x.id) ? x : !x.optional;
                })
                .map((x) => x.id);
        }

        // set the cookie.
        let max_age = (365 * 24 * 60 * 60);

        let secure = window.location.hostname === 'localhost' ? "" : "secure";
        document.cookie = `cookiebanner=${encodeURIComponent(enable_cookies)}; path=/; max-age=${max_age}; ${secure}`;
        location.reload();
    })
});
