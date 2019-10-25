// 个人设置框的显示和隐藏
var count = 1;
$(".settings>img:nth-child(2)").on("click", function(){
  if(count==1){
    $(".settings>div:last-child").css({"display": "block"})
    $(this).attr("src", "../static/images/admin/up.png")
    count = 2
  }else{
    $(".settings>div:last-child").css({"display": "none"})
    $(this).attr("src", "../static/images/admin/down.png")
    count = 1
  }
});
$(".settings>div:last-child").on("click", function(){
    $(this).css({"display": "none"})
    $(".settings>img:nth-child(2)").attr("src", "../static/images/admin/down.png")
    count = 1
});