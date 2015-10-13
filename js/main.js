/* $(function() {
	window.setTimeout(unhide,500);
});
function unhide() {
	$('.shell-inv').removeClass('shell-inv')
}
*/
$(document).ready(function(){
	$('a[href*=#]').click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
			var $target = $(this.hash);
			$target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');
			 if ($target.length) {
			 	var targetOffset = $target.offset().top - 100;
				$('html,body').animate({scrollTop: targetOffset}, 1000);
				return false;
			}
		}
	});
});
setTimeout(function() {
	if($(window).width() > 500) {
		$(".shell-inv").show(function() {
			$(this).find("iframe").prop("src",function(){
				return $(this).data("src");
			});
		});
	}
},1000);
setTimeout(function() {
	$(".shell-inv").removeClass("shell-inv");
},2000);
