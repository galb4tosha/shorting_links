
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
			type: 'POST'
		});
    });
});