$(document).ready(function() {
	$('.contactBttn').click(function(){
		var info = "#CI" + $(this).attr('id');
		if($(info).is(':visible')){
			$(info).fadeOut();
		}
		else{
			$(info).fadeIn();
		}
		
	})
});