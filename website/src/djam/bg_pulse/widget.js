/*
this.colourAt = function (number)
	{
		return calcHex(number, startColour.substring(0,2), endColour.substring(0,2)) 
			+ calcHex(number, startColour.substring(2,4), endColour.substring(2,4)) 
			+ calcHex(number, startColour.substring(4,6), endColour.substring(4,6));
	}
	
	function calcHex(number, channelStart_Base16, channelEnd_Base16)
	{
		var num = number;
		if (num < minNum) {
			num = minNum;
		}
		if (num > maxNum) {
			num = maxNum;
		} 
		var numRange = maxNum - minNum;
		var cStart_Base10 = parseInt(channelStart_Base16, 16);
		var cEnd_Base10 = parseInt(channelEnd_Base16, 16); 
		var cPerUnit = (cEnd_Base10 - cStart_Base10)/numRange;
		var c_Base10 = Math.round(cPerUnit * (num - minNum) + cStart_Base10);
		return formatHex(c_Base10.toString(16));
	}

	function formatHex(hex) 
	{
		if (hex.length === 1) {
			return '0' + hex;
		} else {
			return hex;
		}
	} 
*/

$.widget("snazz.livebg", {
	_create: function() {
		this.data_points = this.option.data || [];
		console.log("Creating live BG on ", this.element, this.options);
	},
	push: function(int) {
		this.data_points.push(int);
		this.data_points = this.data_points.slice(1);
	},
	redraw: function(){
		var ctx = this.element.getContext("2d");
		var grd = ctx.createLinearGradient(0, 0, 170, 0);
		grd.addColorStop(0, "black");
		grd.addColorStop(1, "white");

		ctx.fillStyle = grd;
		ctx.fillRect(20, 20, 150, 100);
	}
})

$( document ).ready(function(){
	$(".bg-pulse").livebg({
		data: [10, 15, 50, 55, 20, 30, 10, 50, 70, 90,
			    0, 10, 20, 20, 30, 25, 40, 30, 70, 20]
	});
});
