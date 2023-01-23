$(document).ready(function() {
    $('.go-to-audit').click(function() {
        window.location.replace('/audit/product/' + $(this).data("go-to-audit"));
    });
});
    
function onBlurTextarea(form){   
    const csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    data = JSON.stringify({"id":form.id, [form.name]:form.value});
    fetch(window.location.pathname, { 
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken
        },
        body: data
      })
      .then()
      .catch((error) => {
        console.log(error);
      });
}

function onChangeSelect(form){
    const csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    data = JSON.stringify({"id":form.id, [form.name]:form.value});
    fetch(window.location.pathname, { 
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken
        },
        body: data
      })
      .then()
      .catch((error) => {
        console.log(error);
      });
}




