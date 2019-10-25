// // 表格操作
// $(".img_edit").hover(function(){
//     $(this).attr("src", "/static/images/word/edit_selected.png")
// },
// function(){
//     $(this).attr("src", "/static/images/word/edit.png")
// });
//
// //查询按钮的点击事件
// $(".management [type=submit]").on("click", function(){
//     $.get("/word/find_by_keyword", function(res){
//         console.log(res)
//         $(".content>.table>tbody").html("")
//         for(var i=0; i < res["total"]; i++){
//             var tr = $("<tr></tr>")
//             tr.append("<td>"+res['words'][i]['id']+"</td>")
//             tr.append("<td>"+res['words'][i]['word']+"</td>")
//             tr.append("<td>"+res['words'][i]['translation']+"</td>")
//             tr.append("<td>"+res['words'][i]['introduction']+"</td>")
//             tr.append("<td>"+res['words'][i]['group_name']+"</td>")
//             tr.append("<td>"+res['words'][i]['add_time']+"</td>")
//             var td1 =  $("<td></td>")
//             for(var j=0; j < res['words'][i]['star']; j++){
//                 td1.append("<img src='/static/images/word/heart_selected.png'>")
//             }
//             for(var j=0; j < 5-res['words'][i]['star']; j++){
//                 td1.append("<img src='/static/images/word/heart.png'>")
//             }
//             tr.append(td1)
//             tr.append("<td class='image'>" +
//                 "<img  data-toggle=\"modal\" data-target=\"#myModal_select\" src='/static/images/word/reading.png'>" +
//                 "<img class=\"img_edit\" data-toggle=\"modal\" data-target=\"#myModal\" src='/static/images/word/edit.png'>" +
//                 "<img data-toggle=\"modal\" data-target=\"#myModal_delete\" src='/static/images/word/delete.png'>" +
//                 "</td>")
//             $(".content>.table>tbody").append(tr)
//         }
//     })
// })
