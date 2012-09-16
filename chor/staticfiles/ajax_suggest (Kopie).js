function searchSuggest(inputString) {
	console.debug("nomz");
	if(inputString.length == 0) {
		// Hide the suggestion box.
	$('#suggestions').hide();
	} else {
	$.get("/kalender/ajax/category_suggest", {str: ""+inputString+""}, function(data){
	if(data.length >0) {
	$('#suggestions').show();
	$('#autoSuggestionsList').html(data);
	}
	});
	}
	}
