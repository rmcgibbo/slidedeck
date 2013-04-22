require(['order!modernizr.custom.45394',
         'order!prettify/prettify', 'order!hammer', 'order!slide-controller',
         'order!slide-deck'], function(someModule) {

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
