$(function(){
	// $(".content").load("/word/show");
	// 导航栏的切换样式
	var lis = $(".myNav>ul li");
	$(".myNav>ul").on("click", function(event){
		lis.each(function(){
			$(this).css({"color": "#b8c7ce","background-color": "#202d33"})
		});
		$(event.target).css({"color":" #f2f2f2","background-color": "#1e282c"})
	});

	// 单词管理面板切换
	// $(".Word").on("click", function(){
	// 	$.get("/word");

		// 加载表格数据
		// $.get("/word/findAll", function(res){
		// 	$(".content>.table>.tbody").html("");
		// 	for(var i=0; i < res["total"]; i++){
		// 		var tr = $("<tr></tr>");
		// 		tr.append("<td>"+res['words'][i]['id']+"</td>");
		// 		tr.append("<td>"+res['words'][i]['word']+"</td>");
		// 		tr.append("<td>"+res['words'][i]['translation']+"</td>");
		// 		tr.append("<td>"+res['words'][i]['introduction']+"</td>");
		// 		tr.append("<td>"+res['words'][i]['group_name']+"</td>");
		// 		tr.append("<td>"+res['words'][i]['add_time']+"</td>");
		// 		var td1 =  $("<td></td>");
		// 		for(var j=0; j < res['words'][i]['star']; j++){
		// 			td1.append("<img src='/static/images/word/heart_selected.png'>")
		// 		}
		// 		for(var j=0; j < 5-res['words'][i]['star']; j++){
		// 			td1.append("<img src='/static/images/word/heart.png'>")
		// 		}
		// 		tr.append(td1);
		// 		tr.append("<td class='image'>" +
		// 			"<img  data-toggle=\"modal\" data-target=\"#myModal_select\" src='/static/images/word/reading.png'>" +
		// 			"<img class=\"img_edit\" data-toggle=\"modal\" data-target=\"#myModal\" src='/static/images/word/edit.png'>" +
		// 			"<img data-toggle=\"modal\" data-target=\"#myModal_delete\" src='/static/images/word/delete.png'>" +
		// 			"</td>");
		// 		$(".content>.table").append(tr);
		// 	}
		// })
	// });

	// 分组管理面板切换
	// $(".Group").on("click", function(){
	//
	// 		$(".content").load("/group/show");
	// 		// 加载表格数据
	// 		$.get("/group/show/all", function(res){
	// 			for(var i=0; i < res["total"]; i++){
	// 				var tr = $("<tr></tr>")
	// 				tr.append("<td>"+res['groups'][i]['id']+"</td>")
	// 				tr.append("<td>"+res['groups'][i]['name']+"</td>")
	// 				tr.append("<td>"+res['groups'][i]['count']+"</td>")
	// 				tr.append("<td>"+res['groups'][i]['add_time']+"</td>")
	// 				tr.append("<td class='image'>" +
	// 					"<img  data-toggle=\"modal\" data-target=\"#myModal_select\" src='/static/images/group/reading.png'>" +
	// 					"<img class=\"img_edit\" data-toggle=\"modal\" data-target=\"#myModal\" src='/static/images/group/edit.png'>" +
	// 					"<img data-toggle=\"modal\" data-target=\"#myModal_delete\" src='/static/images/group/delete.png'>" +
	// 					"</td>")
	// 				$(".content>.table").append(tr)
	// 			}
	// 		})
	// 	}
	// });

	// 个人中心面板切换
	var personal_count = 1;
	$(".Personal").on("click", function(){
		if($(this).next().attr("class") == "sub_ul"){
			if(personal_count==1){
				$(".Personal>img:last-child").attr("src", "/static/images/up.png");
				$(this).next().attr("style","display: block");
				personal_count = 2
			}else{
				$(".Personal>img:last-child").attr("src", "/static/images/down.png");
				$(this).next().attr("style","display: none");
				personal_count = 1
			}
		}else{
			$(".content").load("/personal/show");
		}
	});

	// 反馈管理面板切换
	var feedback_count = 1;
	$(".Feedback").on("click", function(){
		if($(this).next().attr("class") == "sub_ul"){
			if(feedback_count==1){
				$(".Feedback>img:last-child").attr("src", "./static/images/up.png");
				$(this).next().attr("style","display: block");
				feedback_count = 2
			}else{
				$(".Feedback>img:last-child").attr("src", "./static/images/down.png");
				$(this).next().attr("style","display: none");
				feedback_count = 1
			}
		}else{
			$(".content").load("/feedback/show");
		}
	});

	// 关于我们面板切换
	var about_count = 1;
	$(".About").on("click", function(){
		if($(this).next().attr("class") == "sub_ul"){
			if(about_count==1){
				$(".About>img:last-child").attr("src", "./static/images/up.png");
				$(this).next().attr("style","display: block");
				about_count = 2
			}else{
				$(".About>img:last-child").attr("src", "./static/images/down.png");
				$(this).next().attr("style","display: none");
				about_count = 1
			}
		}else{
			$(".content").load("/about/show");
		}
	});

	// 用户设置的显示与隐藏
	var user_count = 1;
	$(".settings>img:nth-child(4),.settings>span:nth-child(5),.settings>img:nth-child(6)").on("click", function(){
		if(user_count == 1){
			$(".user").css({"display": "block"});
			$(".settings>img:nth-child(6)").attr("src", "/static/images/title_up.png");
			user_count = 2
		}else{
			$(".user").css({"display": "none"});
			$(".settings>img:nth-child(6)").attr("src", "/static/images/title_down.png");
			user_count = 1
		}
	});

	// 用户设置面板的样式控制
	var user_lis = $(".user li");
	$(".user li").hover(function(event){
		user_lis.each(function(){
			$(this).css({"background-color": "white", "color": "#717171"})
		});
		$(event.target).css({"background-color": "#5d6dc3", "color": "white"})
		$(event.target).on("click", function(){
			if($(this).context.innerText === "个人设置"){
				$(".content").load("/personal/show")
			}
			else if ($(this).context.innerText === "密码设置") {
				$(".content").load("/personal/show")
			}
			$(".user").css({"display": "none"});
			$(".settings>img:nth-child(6)").attr("src", "/static/images/title_down.png");
			user_count = 1
		})
	});
});