requirejs.config({
    baseUrl: "js/",
    paths: {
	modernizer: "modernizr.custom.45394",
	prettify: "https://cdnjs.cloudflare.com/ajax/libs/prettify/r298/prettify.min",
	underscore: "https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.7.0/underscore-min",
	hammer: "https://cdnjs.cloudflare.com/ajax/libs/hammer.js/0.6.4/hammer.min"
    },
    shim:  {
	'slide-deck' : {
	    deps: ['modernizer', 'hammer', 'underscore'],
	    exports: 'SlideDeck',
	},
	'modernizer' : 'Modernizr',
	'hammer': {exports: 'Hammer'},
    }	
});

require(['modernizer', 'prettify', 'hammer', 'slide-controller',
	 'slide-deck'],function(someModule) {

var initElasticity = function() {    
    var resize = function() {
    	var slidesEl = document.getElementsByTagName('slides')[0];
    	
    	minWidth = slidesEl.offsetWidth;
    	minHeight = slidesEl.offsetHeight;
    
        if (window.innerWidth < minWidth || window.innerHeight < minHeight) {
            var sx = window.innerWidth / minWidth;
            var sy = window.innerHeight / minHeight;
            var transform = "scale(" + Math.min(sx, sy) + ")";
        } else {
            var transform = "none";
        }
        
        slidesEl.style.MozTransform = transform;
        slidesEl.style.WebkitTransform = transform;
        slidesEl.style.OTransform = transform;
        slidesEl.style.msTransform = transform;
        slidesEl.style.transform = transform;
    }   
    
    resize();
    window.onresize = resize;
};        

if (document.readyState === "complete") {
  initElasticity();
} else {
  window.addEventListener("load", initElasticity);
}

});
