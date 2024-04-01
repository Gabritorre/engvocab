function type(string, container_id, speed = 1) {

	let interval = 150;
	if (speed == 1) {
		interval = 150;
	}
	else if (speed == 2) {
		interval = 100;
	}
	else if (speed == 3) {
		interval = 40;
	}
	console.log(interval)
	let container = document.getElementById(container_id);
	container.innerHTML = "";
	for (let i = 0; i < string.length; i++) {
		setTimeout(() =>{
			container.innerHTML += string[i];
		}, i * interval);
	}
}

function AddEvents() {
	var nav_items = document.getElementsByClassName('nav_item');

	for (let i = 0; i < nav_items.length; i++) {
		nav_items[i].addEventListener('mouseover', run_typing);
		nav_items[i].addEventListener('mouseout', clear_command);
	}
}

function clear_command(e) {
	let container = document.getElementById("command");
	container.innerHTML = "";
}

function run_typing(e) {
	type(this.innerHTML.toLowerCase(), "command", 3)
}

