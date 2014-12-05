(function($){

	/* ---------------------------------------------- /*
	 * Preloader
	/* ---------------------------------------------- */

	$(window).load(function() {
		$('#status').fadeOut();
		$('#preloader').delay(350).fadeOut('slow');
		$('body').delay(350).css({'overflow':'visible'});
	});

	$(document).ready(function() {

		/* ---------------------------------------------- /*
		 * Background image
		/* ---------------------------------------------- */

		$.backstretch([
			'assets/images/bg2.jpg',
			'assets/images/bg1.jpg',
			'assets/images/bg3.jpg'
		], {duration: 3000, fade: 750});

		/* ---------------------------------------------- /*
		 * Animation scroll
		/* ---------------------------------------------- */

		$('a[href*=#]').bind('click', function(e) {
			var anchor = $(this);

			$('html, body').stop().animate({
				scrollTop: $(anchor.attr('href')).offset().top
			}, 500);
			e.preventDefault();
		});

		/* ---------------------------------------------- /*
		 * WOW Animation When You Scroll
		/* ---------------------------------------------- */

		wow = new WOW({
			mobile: false
		});
		wow.init();

		/* ---------------------------------------------- /*
		 * TimeCicles
		/* ---------------------------------------------- */

		var countdown =  $('.countdown-time');

		createTimeCicles();

		$(window).on('resize', windowSize);

		function windowSize(){
			countdown.TimeCircles().destroy();
			createTimeCicles();
			countdown.on('webkitAnimationEnd mozAnimationEnd oAnimationEnd animationEnd', function() {
				countdown.removeClass('animated bounceIn');
			});
		}

		function createTimeCicles() {
			countdown.addClass('animated bounceIn');
			countdown.TimeCircles({
				fg_width: 0.013,
				bg_width: 0.6,
				circle_bg_color: '#ffffff',
				time: {
			         Hours: {color: '#19B5FE'}
				,	 Minutes: {color: '#19B5FE'}
				,	 Seconds: {color: '#19B5FE'}
				}
			});
			countdown.on('webkitAnimationEnd mozAnimationEnd oAnimationEnd animationEnd', function() {
				countdown.removeClass('animated bounceIn');
			});
		}

		/* ---------------------------------------------- /*
		 * Subscribe form ajax
		/* ---------------------------------------------- */

		$(".subscription-form").submit(function(e) {

			e.preventDefault();

			var email = $("#sub-email").val();
			var dataString = 'email=' + email;

			$.ajax({
				type: "POST",
				url: "assets/php/subscribe.php",
				data: dataString,
				dataType: 'json',
				success: function (result) {
					if(result.formstatus == 1) {
						$('.subscription-message').html(result.message);
						$('.subscription-message').fadeIn(500);
						$('.subscription-form').fadeOut(500);
					} else {
						$('.subscription-message').html(result.message);
						$('.subscription-message').fadeIn(1000);
					}
				}
			});

			return false;

		});

	});

})(jQuery);
