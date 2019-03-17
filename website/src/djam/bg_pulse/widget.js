
String.prototype.format = function() {
    a = this;
    for (k in arguments) {
        a = a.replace("{" + k + "}", arguments[k])
    }
    return a
}

$.widget("snazz.livebg", {
	_create: function() {
		this.data = this.options.data || [];
		this.max = this.options.max || 100;
		this.min = this.options.min || 0;
		this.slots = this.options.slots;
		this.frequency = this.options.frequency || 1000;

		var color = this.options.bg_color || "990000";
		this.color = {
			r: parseInt(color.substring(0, 2), 16),
			g: parseInt(color.substring(2, 4), 16),
			b: parseInt(color.substring(4, 6), 16),
		}
		console.log("Rect is", this.element.width(), "x", this.element.height());
		this.reset_gradient();
	},
	update: function(int) {
		this.data.push(int);
		//this.data = this.data.slice(1);
		//this.update();
	},

	build_gradient: function(){
		var points = this.data.length;
		interval_width = this.element.width() / this.slots;
		percent_steps = 100 / (this.slots);
		//console.log(points, "data points", interval_width, "width", percent_steps, "% per point", this.data);

		var color_points = [];
		var offset = 0;
		for (var i = 0; i < this.data.length; i++){
			var opacity = (this.data[i] / this.max).toFixed(2);
			//offset = offset + percent_steps
			offset += interval_width;
			//console.log("{0} val:{1} opa:{2} {3}px".format(i, this.data[i], opacity, offset));
			color_points.push(
				"rgba({0}, {1}, {2}, {3}) {4}px".format(
					this.color.r,
					this.color.g,
					this.color.b,
					opacity,
					offset
			));
		}
		return {gradient: color_points, size: offset};
	},

	reset_gradient: function(){
		var bg_info = this.build_gradient();
		var interval_width = Math.floor(this.element.width() / this.slots);
		this.element.css({
			background: "linear-gradient(to right, {0})".format(bg_info.gradient.join(",")),
			backgroundSize: bg_info.size
		});
		var distance = "-={0}px".format(interval_width);
		//console.log("Animating: {0} for {1}s".format(distance, this.frequency))
		
		this.element.animate({
			backgroundPositionX: distance
		}, this.frequency, "linear", function(){
			this.data = this.data.slice(1);
			//this.reset_gradient();
		}.bind(this));
		
	},
})


