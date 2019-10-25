$(function(){
    $(".replaced").load("user.html");

    // 导航栏的切换
    var $lis = $(".myNav li")
    $(".myNav>ul").on("click", function(event){
    	$lis.each(function(){
    		$(this).css({
    			"font-size": "18px",
    		});
    	})
    	$(event.target).css({
    			"font-size": "22px",
    		})
    });

    // 用户管理的切换
    $(".user_page").on("click", function(){
        $(".replaced").load("user.html")
    });

    // 反馈管理的切换
    $(".feedback_page").on("click", function(){
        $(".replaced").load("feedback.html")
    });
});