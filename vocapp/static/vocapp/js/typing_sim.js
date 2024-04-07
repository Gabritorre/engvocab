timers = []
function type(string, container_id, speed = 1) {
	let interval = 150;
	if (speed == 1) {
		interval = 135;
	}
	else if (speed == 2) {
		interval = 100;
	}
	else if (speed == 3) {
		interval = 40;
	}
	let container = document.getElementById(container_id);
	container.innerHTML = "";

	for(let i = 0; i < timers.length; i++) {
		clearTimeout(timers[i]);
	}

	for (let i = 0; i < string.length; i++) {
		timers[i] = setTimeout(() =>{
			container.innerHTML += string[i];
		}, i * interval);
	}
}

function AddEvents() {
	var nav_items = document.getElementsByClassName('nav_item');

	for (let i = 0; i < nav_items.length; i++) {
		nav_items[i].addEventListener('mouseover', function() {
			type("cd /" + nav_items[i].innerHTML.toLowerCase(), "command", 3);
		});
		nav_items[i].addEventListener('mouseout', clear_command);
	}
}

function clear_command(e) {
	for(let i = 0; i < timers.length; i++) {
		clearTimeout(timers[i]);
	}
	let container = document.getElementById("command");
	container.innerHTML = "";
}


