$(document).ready(function(){
    $("div.collapsible").mouseover(function(){
        $(this).addClass("collapsible-border");
    }).mouseout(function(){
        $(this).removeClass("collapsible-border");
    }).click(function(){
		if ($("div#body").hasClass("expand")) {
			$("div#body").removeClass("expand");
		} else {
			$("div#body").addClass("expand");
		}
    });
    
    $(".action.close").click(function(){
        $(this).parents("ul.ullist").animate({
            opacity: "hide"
        }, "slow");
    });
//    $(".action.delete").click(function(){
//        $(this).parents("ul.ullist li").animate({
//            opacity: "hide"
//        }, "slow");
//    });

//commenting out the light-box behaviour.
//    $(".action.delete").fancybox({
//        'titleShow': false,
//        'transitionIn': 'fade',
//        'transitionOut': 'fade'
//    });
    $("div.buttons a.no").click(function(){
        $.fancybox.close();
    });
    $("div.buttons a.yes").click(function(e){
        $(this).parents("ul.ullist li").animate({
            opacity: "hide"
        }, "slow");
        $.fancybox.close();
    });
    
    $(".action.summary").click(function(){
        $(this).parents("ul.ulaction").siblings("div.quiz-summary").slideToggle("slow");
        $(this).toggleClass("active");
    });
    $("ul.quizlt a.action").tipsy({
        fade: true,
        delayIn: 0,
        delayOut: 0,
    });
    
    $("div.quizOverViewContainer a.question").tipsy({
        fade: true
    });
    
    $("li.template a.thumb").click(function(){
        $("li.template a.thumb img").css('border', '1px #DDDDDD solid');
        $(this).children("img").css('border', '2px solid red');
    });
    $("li.template a.thumb").tipsy({
        fade: true
    });
    $("li.buttons a").tipsy({
        fade: true
    });
});
