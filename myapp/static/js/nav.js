$('.menu li a').on('click', function(){
    $('li a.active').removeClass('active');
    $(this).addClass('active');
});
// $(document).ready(function(){
//     $('men').click(function(){
//    		 $('men').removeClass("active");
//    		 $(this).addClass("active");
// 		});
// });

