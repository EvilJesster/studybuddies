function hell(){
	$('button').click(function(){
		var message = $('#message').val();
		$.ajax ({
			url: '/messagingback',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
};