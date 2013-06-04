$(document).ready(function() {
	var mainUrl = "http://127.0.0.1:8000/main/";
	$('#initPg #srchBttn').click(function() {
		document.location = mainUrl + "results"
	});

	$('#rltsTtl').click(function() {
		document.location = mainUrl
	});
});