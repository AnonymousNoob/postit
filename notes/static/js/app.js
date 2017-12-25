// delete Note
function deleteNote(noteId){
	$.ajax({
	    url: "notes/"+noteId,
	    type:"DELETE",
  	}).done(function(data){
	  	var target = "/";
	    $("#wrapper").load(target, function() {
		});
	});
}

// add Note
function addNote(){
	$.ajax({
	    url: "notes/create/",
	    type:"POST",
  	}).done(function(data){
  		var target = "/";
	    $("#wrapper").load(target, function() {
		});
  	});
}
