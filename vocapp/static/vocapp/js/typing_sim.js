var timers = [];
function type(string, container_id, speed = 1, append = false, save = false) {
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
	else if (speed == 4) {
		interval = 20;
	}
	else if (speed == 5) {
		interval = 1;
	}
	let container = document.getElementById(container_id);
	if (!append){
		container.innerHTML = "";
	}

	for(let i = 0; i < timers.length; i++) {
		clearTimeout(timers[i]);
	}

	for (let i = 0; i < string.length; i++) {
		timers[i] = setTimeout(() =>{
			container.innerHTML += string[i];
			if (save) {
				window.filter_command = container.innerHTML;
			}
		}, i * interval);
	}
}


function addNavEvents() {
	var nav_items = document.getElementsByClassName('nav_item');

	for (let i = 0; i < nav_items.length; i++) {
		nav_items[i].addEventListener('mouseover', function() {
			type("cd /" + nav_items[i].innerHTML.toLowerCase(), "command", 3);
		});
		nav_items[i].addEventListener('mouseout', clear_command);
	}
}

function addFilterEvents() {
	var filters = document.getElementsByClassName('filter');

	for (let i = 0; i < filters.length; i++) {
		filters[i].addEventListener('change', buildFilterCommand);
	}

	var apply_button = document.getElementById("apply_filter");
	apply_button.addEventListener("click", function() {
		type(window.filter_command, "command", 5, false, false);
	})
}

function replaceAt(string, index, replacement) {
	if (replacement == ""){
		return string.substring(0, index) + replacement + string.substring(index + replacement.length + 1);
	}
    return string.substring(0, index) + replacement + string.substring(index + replacement.length);
}

function buildFilterCommand(e) {
	interval = 30;
	let container = document.getElementById("command");
	if (e.currentTarget.checked){
		if (window.filter_command.trim() == "") {
			type("filter " + this.value, "command", 3, false, true)
		}
		else {
			if (container.innerHTML.trim() == "") {
				type(window.filter_command + " " + this.value, "command", 3, true, true)
			}
			else {
				type(" " + this.value, "command", 3, true, true)
			}
		}
	}
	else {
		if (container.innerHTML.trim() == ""){
			window.filter_command = window.filter_command.replace(" " + this.value, '');
			type(window.filter_command, "command", 3, false, false)
		}
		else {
			let start_index = window.filter_command.indexOf(" " + this.value);
			window.filter_command = window.filter_command.replace(" " + this.value, '');
			let j = 0;
			interval = 30;
			for (let i = this.value.length; i >= 0; i--) {
				timers[j] = setTimeout(() => {
					container.innerHTML = replaceAt(container.innerHTML, start_index + i, '');
				}, j * interval);
				j++;
			}
		}
	}
}

function clear_command(e) {
	for(let i = 0; i < timers.length; i++) {
		clearTimeout(timers[i]);
	}
	let container = document.getElementById("command");
	container.innerHTML = "";
}


