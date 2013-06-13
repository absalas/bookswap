$(document).ready(function() {
	$('#addPost').click(function(){
		if ($('#postForm').is(':visible')){
			$('#postForm').fadeOut();
		}
		else{
			if ($('#results').is(':visible')){
				$('#results').fadeOut();
			}
			$('#postForm').delay(300).fadeIn();
		}
	});

	$('#viewPost').click(function(){
		if ($('#results').is(':visible')){
			$('#results').fadeOut();
		}
		else{
			if ($('#postForm').is(':visible')){
				$('#postForm').fadeOut();
			}
			$('#results').delay(300).fadeIn();
		}
	});

});