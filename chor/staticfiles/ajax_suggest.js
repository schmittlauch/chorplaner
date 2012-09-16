$(document).ready(console.debug("Test"));

function suggest_req(inputString) {
	console.debug("nomz");
	if(inputString.length == 0) {
		// Hide the suggestion box.
	$('#suggestions').hide();
	} else {
	$.get(dat.target, {str: ""+inputString+""}, function(data){
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
		suggest += "<li onclick='fill(\"" + rstr[i] + "\")'>" + rstr[i] + "</li>";
	}
	suggest += "</ul>";
	console.debug(suggest);
	return(suggest);
}

function fill(thisValue) {
		$(dat.inputid).val(thisValue);
		setTimeout("$('#suggestions').hide();", 200);
	}
