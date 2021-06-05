
$(document).ready(function () {
    // отправка на сервер введенного url
    $("#get-short").on('click', function () {
        if (!$('#input-url').val()) {
			return;
		}
        let long_url = $('#input-url').val();
        $.ajax({
			url         : 'http://127.0.0.1:5000/',
			data: long_url,
			cache: false,
			processData: false,
			contentType: false,
			type: 'POST',
            success: function (respond) {
                let output_link_div = document.createElement("div");
                output_link_div.className = "output-url";
                document.body.appendChild(output_link_div);
                
                short_link = document.createElement("a");
                short_link.href = respond;
                short_link.innerHTML = respond;
                output_link_div.appendChild(short_link);

                console.log(respond);
                // $("#output-url").append(
                //     `<a href = "${respond}"> ${respond} </a>`
                // );
            }
		});
    });
});