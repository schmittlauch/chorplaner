$(document).ready(alert("Trololo"));
function suggest(inputString) {
	console.debug("nomz");
	if(inputString.length == 0) {
		// Hide the suggestion box.
	$('#suggestions').hide();
	} else {
	$.get("/kalender/ajax/category_suggest", {str: ""+inputString+""}, function(data){
	if(data.length >0) {
	$('#suggestions').show();
	$('#autoSuggestionsList').html(response_to_li(data));
	}
	});
	}
}

function response_to_li(response) {
	var rstr = response.split("\n");
	suggest = '<ul>';
	for(i=0; i < rstr.length - 1; i++) {
		suggest += "<li onclick='fill(\"" + rstr[i] + "\")>" + rstr[i] + "</li>"
	}
	suggest += "</ul>
	return(suggest)
}

function fill(thisValue) {
		$('#category_suggest').val(thisValue);
		setTimeout("$('#suggestions').hide();", 200);
	}
