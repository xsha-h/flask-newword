// // 难度系数导航栏切换
// var rank_lis = $(".rank_ul>li")
// $(".rank_ul").on("click", function(event){
//     rank_lis.each(function(){
//         $(this).css({"color": "black"})
//     });
//     $(event.target).css({"color": "#4ac883"})
// });
//
// // 导航栏的点击事件
// $(".rank_ul>li:first-child").on("click", function(){
//     $("#chart_changed1").css("display", "block")
//     $("#chart_changed2").css("display", "none")
// })
// $(".rank_ul>li:last-child").on("click", function(){
//     $("#chart_changed1").css("display", "none")
//     $("#chart_changed2").css("display", "block")
// })
//
// // 文章统计导航栏切换
// var day_lis = $(".day_ul>li")
// $(".day_ul").on("click", function(event){
//     day_lis.each(function(){
//         $(this).css({"color": "black"})
//     });
//     $(event.target).css({"color": "#4ac883"})
// });
//
// // 导航栏的点击事件
//
// $(".day_ul>li:first-child").on("click", function(){
//     $("#day_changed1").css("display", "block")
//     $("#day_changed2").css("display", "none")
//     $("#day_changed3").css("display", "none")
//     $("#day_changed4").css("display", "none")
// })
// $(".day_ul>li:nth-child(2)").on("click", function(){
//     $("#day_changed1").css("display", "none")
//     $("#day_changed2").css("display", "block")
//     $("#day_changed3").css("display", "none")
//     $("#day_changed4").css("display", "none")
// })
// $(".day_ul>li:nth-child(3)").on("click", function(){
//     $("#day_changed1").css("display", "none")
//     $("#day_changed2").css("display", "none")
//     $("#day_changed3").css("display", "block")
//     $("#day_changed4").css("display", "none")
// })
// $(".day_ul>li:last-child").on("click", function(){
//     $("#day_changed1").css("display", "none")
//     $("#day_changed2").css("display", "none")
//     $("#day_changed3").css("display", "none")
//     $("#day_changed4").css("display", "block")
// })
//
//
//
// // 数据统计导航栏切换
// var group_lis = $(".group_ul>li")
// $(".group_ul").on("click", function(event){
//     group_lis.each(function(){
//         $(this).css({"color": "black"})
//     });
//     $(event.target).css({"color": "#4ac883"})
// });
//
// // 导航栏的点击事件
//
// $(".group_ul>li:first-child").on("click", function(){
//     $("#group_changed1").css("display", "block")
//     $("#group_changed2").css("display", "none")
// })
// $(".group_ul>li:last-child").on("click", function(){
//     $("#group_changed1").css("display", "none")
//     $("#group_changed2").css("display", "block")
// })
//
//
// // 英文难度系数概览图
// var chart = Highcharts.chart('chart_changed1', {
//     chart: {
//         polar: true,
//         type: 'line'
//     },
//     title: {
//         text: '英文难度系数',
//         x: -80
//     },
//     pane: {
//         size: '80%'
//     },
//     xAxis: {
//         categories: ['5星', '3星', '1星', '0星',
//                      '2星', '4星'],
//         tickmarkPlacement: 'on',
//         lineWidth: 0
//     },
//     yAxis: {
//         gridLineInterpolation: 'polygon',
//         lineWidth: 0,
//         min: 0
//     },
//     tooltip: {
//         shared: true,
//         pointFormat: '<span style="color:{series.color}">{series.name}: <b>${point.y:,.0f}</b><br/>'
//     },
//     legend: {
//         align: 'right',
//         verticalAlign: 'top',
//         y: 70,
//         layout: 'vertical'
//     },
//     series: [{
//         name: '期望难度系数',
//         data: [43, 40, 60, 75, 70, 50],
//         pointPlacement: 'on'
//     }, {
//         name: '实际难度系数',
//         data: [20, 45, 42, 30, 56, 60],
//         pointPlacement: 'on'
//     }]
// });
//
// //英文难度系数详细图
// var chart = Highcharts.chart('chart_changed2', {
//     chart: {
//         type: 'column'
//     },
//     title: {
//         text: '每个星级难度的单词数量'
//     },
//     subtitle: {
//         text: '请点击按钮查看坐标轴变化'
//     },
//     xAxis: {
//         categories: ['无星', '一星', '二星', '三星', '四星', '五星']
//     },
//     yAxis: {
//         labels: {
//             x: -15
//         },
//         title: {
//             text: '个数'
//         }
//     },
//     series: [{
//         name: '星级',
//         data: [43, 52, 34, 78, 56, 84]
//     }],
//     responsive: {
//         rules: [{
//             condition: {
//                 maxWidth: 500
//             },
//             // Make the labels less space demanding on mobile
//             chartOptions: {
//                 xAxis: {
//                     labels: {
//                         formatter: function () {
//                             return this.value.replace('月', '')
//                         }
//                     }
//                 },
//                 yAxis: {
//                     labels: {
//                         align: 'left',
//                         x: 0,
//                         y: -2
//                     },
//                     title: {
//                         text: ''
//                     }
//                 }
//             }
//         }]
//     }
// });
//
// // 一周文章统计的总计量
// var chart = Highcharts.chart('day_changed1', {
//     chart: {
//         type: 'line'
//     },
//     title: {
//         text: '单词统计量'
//     },
//     subtitle: {
//         text: ''
//     },
//     xAxis: {
//         categories: ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
//     },
//     yAxis: {
//         title: {
//             text: '个数（个）'
//         }
//     },
//     plotOptions: {
//         line: {
//             dataLabels: {
//                 // 开启数据标签
//                 enabled: true
//             },
//             // 关闭鼠标跟踪，对应的提示框、点击事件会失效
//             enableMouseTracking: false
//         }
//     },
//     series: [{
//         name: '收藏',
//         data: [15, 20, 29, 17, 18, 21, 25]
//     }, {
//         name: '标记',
//         data: [20, 30, 20, 27, 15, 31, 15]
//     }, {
//         name: '牢记',
//         data: [10, 5, 12, 13, 10, 21, 11]
//     }]
// });
//
// // 一周的单词收藏量
// var chart = Highcharts.chart('day_changed2', {
//     chart: {
//         type: 'column'
//     },
//     title: {
//         text: '一周的单词收藏量'
//     },
//     subtitle: {
//         text: '请点击按钮查看坐标轴变化'
//     },
//     xAxis: {
//         categories: ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
//     },
//     yAxis: {
//         labels: {
//             x: -15
//         },
//         title: {
//             text: '个数'
//         }
//     },
//     series: [{
//         name: '星级',
//         data: [6, 8, 15, 7, 10, 13, 9]
//     }],
//     responsive: {
//         rules: [{
//             condition: {
//                 maxWidth: 500
//             },
//             // Make the labels less space demanding on mobile
//             chartOptions: {
//                 xAxis: {
//                     labels: {
//                         formatter: function () {
//                             return this.value.replace('月', '')
//                         }
//                     }
//                 },
//                 yAxis: {
//                     labels: {
//                         align: 'left',
//                         x: 0,
//                         y: -2
//                     },
//                     title: {
//                         text: ''
//                     }
//                 }
//             }
//         }]
//     }
// });
//
// // 一周的单词标记量
// var chart = Highcharts.chart('day_changed3', {
//     chart: {
//         type: 'column'
//     },
//     title: {
//         text: '一周的单词标记量'
//     },
//     subtitle: {
//         text: '请点击按钮查看坐标轴变化'
//     },
//     xAxis: {
//         categories: ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
//     },
//     yAxis: {
//         labels: {
//             x: -15
//         },
//         title: {
//             text: '个数'
//         }
//     },
//     series: [{
//         name: '星级',
//         data: [16, 28, 35, 27, 20, 23, 19]
//     }],
//     responsive: {
//         rules: [{
//             condition: {
//                 maxWidth: 500
//             },
//             // Make the labels less space demanding on mobile
//             chartOptions: {
//                 xAxis: {
//                     labels: {
//                         formatter: function () {
//                             return this.value.replace('月', '')
//                         }
//                     }
//                 },
//                 yAxis: {
//                     labels: {
//                         align: 'left',
//                         x: 0,
//                         y: -2
//                     },
//                     title: {
//                         text: ''
//                     }
//                 }
//             }
//         }]
//     }
// });
//
// // 一周的单词牢记量
// var chart = Highcharts.chart('day_changed4', {
//     chart: {
//         type: 'column'
//     },
//     title: {
//         text: '一周的单词牢记量'
//     },
//     subtitle: {
//         text: '请点击按钮查看坐标轴变化'
//     },
//     xAxis: {
//         categories: ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
//     },
//     yAxis: {
//         labels: {
//             x: -15
//         },
//         title: {
//             text: '个数'
//         }
//     },
//     series: [{
//         name: '星级',
//         data: [6, 8, 5, 7, 10, 3, 9]
//     }],
//     responsive: {
//         rules: [{
//             condition: {
//                 maxWidth: 500
//             },
//             // Make the labels less space demanding on mobile
//             chartOptions: {
//                 xAxis: {
//                     labels: {
//                         formatter: function () {
//                             return this.value.replace('月', '')
//                         }
//                     }
//                 },
//                 yAxis: {
//                     labels: {
//                         align: 'left',
//                         x: 0,
//                         y: -2
//                     },
//                     title: {
//                         text: ''
//                     }
//                 }
//             }
//         }]
//     }
// });
//
// // 数据统计分组概览图
// var chart = Highcharts.chart('group_changed1', {
//     chart: {
//         plotBackgroundColor: null,
//         plotBorderWidth: null,
//         plotShadow: false,
//         type: 'pie'
//     },
//     title: {
//         text: '单词分组量'
//     },
//     tooltip: {
//         pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
//     },
//     plotOptions: {
//         pie: {
//             allowPointSelect: true,
//             cursor: 'pointer',
//             dataLabels: {
//                 enabled: true,
//                 format: '<b>{point.name}</b>: {point.percentage:.1f} %',
//                 style: {
//                     color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
//                 }
//             }
//         }
//     },
//     series: [{
//         name: 'Brands',
//         colorByPoint: true,
//         data: [{
//             name: '形容词',
//             y: 40.5
//         }, {
//             name: '动词',
//             y: 20.5
//         }, {
//             name: '名词',
//             y: 18
//         }, {
//             name: '副词',
//             y: 12
//         }, {
//             name: '未知',
//             y: 9
//         }]
//     }]
// });
