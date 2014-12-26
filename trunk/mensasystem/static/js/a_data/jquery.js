/*!jQuery Circular CountDown*/
/*Downward compatible
 * Version: 1.0.0 (26/04/2013)
 * Requires: jQuery v1.7+
 * Copyright (c) 2013 Nikhil Navadiya
 * Thanks to http://www.javascriptkit.com/
 */
(function($) {
	$.fn.ccountdown = function(_yr, _m, _d, _t) {
		var $this = this;
		var _today = new Date();
		// calling function first time so that it wll setup remaining time

		var _changeTime = function() {
			var _today = new Date();
//
			var _todayh = _today.getHours();
			var _todaymin = _today.getMinutes();
			var _todaysec = _today.getSeconds();
			_dhour = Math.floor(_todayh);
			_dmin = Math.floor(_todaymin);
			_dsec = Math.floor(_todaysec);
			var el = $($this);
			var $ss = el.find(".second"), $mm = el.find(".minute"), $hh = el.find(".hour");

            $ss.val(_dsec).trigger("change");
			$mm.val(_dmin).trigger("change");
			$hh.val(_dhour).trigger("change");
};
		_changeTime();
		setInterval(_changeTime, 1000);
	};
 
})(jQuery);

