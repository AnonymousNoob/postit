$(document).ready(function(){
// fetch version
	$('.created').click(function(){
		var version_id = $(this).children('#version_id').val();
		var n = $(this).parents('.note');
		var title = n.find('#title');
		var content = n.find('#content');
		$('.selected').removeClass('selected');
		$(this).addClass('selected');
				$.ajax({
					    url: "notes/version/"+version_id,
					    type:"GET",
				}).done(function(data){
						  	title.val(data["title"]);
						  	content.val(data["content"]);
				});
	});

});