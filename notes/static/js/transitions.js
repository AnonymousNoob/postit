var zIndex=10;
$(document).ready(function(){
	// reveal versions
	$('.versions').click(function(){
        var n = $(this).parents('.note');
        n.find('.version_history').toggle("slide",{ direction: 'left' },10);
        n.find('.contents').toggleClass("coloumn");
        n.find('.version_history').toggleClass("coloumn");
    });  		
    // enlarge notes
	$('.expand').click(function(){
        var n = $(this).parents('.note');
        // close expanded notes
	    if(!n.hasClass('expand_note')){
            $('.expand_note .version_history').toggle();
            $('.expand_note .contents').removeClass("coloumn");
            $('.expand_note').removeClass('expand_note');
        }
        n.find('.contents').removeClass("coloumn");
        n.find('.contents').css('zIndex', zIndex++);
        n.find('.version_history:visible').toggle();
        n.find('.ui-icon').css('zIndex', zIndex++);
        n.toggleClass('expand_note');
        n.find('.versions').toggle("slow");
    });

});