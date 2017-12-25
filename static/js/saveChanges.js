$(document).ready(function(){
// delay after typing
	var delay = (function(){
	  var timer = 0;
	  return function(callback, ms){
	    clearTimeout (timer);
	    timer = setTimeout(callback, ms);
	  };
	})();


// save changes
  	$('#notesCollection > #thread').children().each(function() {
  		// alert($(this).attr('id'));
	  	$(this).on('keyup',function () {
	  	 	var id = $(this).parent().children('#noteId').val();
	  	 	var title = $(this).children('#title').val();
		  	var content = $(this).children('#content').val();
	  	 	delay(function(){
			    $.ajax({
				    url: "notes/update/"+id,
				    type:"PUT",
				    data: {
				    	title:title,
				    	content:content,
					    },
				}).done(function(data){
					  	var target = "autosaveAlert";
						$(".messages").load(target, function() {
							$(".messages").show(0).delay(2000).hide(0); 
			    		});
					});
			},5000);
		});
	});

});