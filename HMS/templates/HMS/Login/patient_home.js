var rss = document.getElementById('rssContainer');
var nodes = document.getElementByTagName('ul');
var select = document.getElementById('showRss');

function hideAll(){
	for(i=0; i<nodes.length;++i){
		nodes[i].style.display='none';
	}
}

select.onchange = function(){
	hideAll();
	var e = this[this.selectedIndex].getAttribute('name');
	var show = document.getElementById(e);
	show.style.display = 'block';
}

hideAll();