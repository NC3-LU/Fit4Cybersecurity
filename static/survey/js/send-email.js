$(document).ready(function() {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  $('.send-email-to-cases').click(function() {
    const subject = encodeURIComponent($(this).data('subject'));
    const body = encodeURIComponent($(this).data('body'));

    window.location.href = "mailto:opensource@nc3.lu?subject=" + subject + "&body=" + body;
  });


  $('.send-report-via-email').click(function() {
    email = document.getElementById("email-input").value
    data = JSON.stringify({"email-address": email});
    lang = document.getElementById("modal-send-report").getAttribute("lang");
    const csrftoken = getCookie('csrftoken');
    fetch("/survey/report/"+lang, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken
      },
      body: data
    })
    .then(res => {
      console.log('Success.');
    })
    .catch((error) => {
      console.log("Error");
    });
    $('#modal-send-report').modal('hide')
  });
});
