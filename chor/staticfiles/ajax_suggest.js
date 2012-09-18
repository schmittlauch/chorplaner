/*Copyright (C) 2012  Oliver Schmidt
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.*/

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
