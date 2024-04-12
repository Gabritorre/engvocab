var timers = [];
var active_timers = 0;		//acts like a semaphore for waiting the previous command to be fully typed into the shell

/*
write a string into a container simulating a real typing
@string: the string to be written
@container_id: the field id of the html tag where the command need to be typed
@speed: the speed of the simulated typing, range from 1 (slowest) to 5 (fastest)
@append: set to true if you want to clear the current content of the container
@save: set to true if you want to store the @stirng into the global variable window.filter_command
@wait: set to true if you want to wait the previous command(s) to finish
*/
async function type(string, container_id, speed = 1, append = false, save = false, wait = false) {
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

	if (wait){
		while (active_timers > 0) {	//wait the termination of the previous command
			await new Promise(r => setTimeout(r, interval));
		}
	}
	else {
		for (let i = 0; i < timers.length; i++) {
			clearTimeout(timers[i]);
		}
	}

	for (let i = 0; i < string.length; i++) {
		active_timers++;
		timers[i] = setTimeout(() => {
			container.innerHTML += string[i];
			if (save) {
				window.filter_command = container.innerHTML;
			}
			if (i == string.length-1) {
				last_timer_begin_time = (new Date()).getTime();
				timer_len = i * interval;
			}
			active_timers--;
		}, i * interval);
	}
}


function addNavEvents() {
	var nav_items = document.getElementsByClassName('nav_item');

	for (let i = 0; i < nav_items.length; i++) {
		nav_items[i].addEventListener('mouseover', function() {
			type("cd /" + nav_items[i].innerHTML.toLowerCase(), "command", 3, false, false, false);
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
		type(window.filter_command, "command", 5, false, false, false);
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
	// add filter this.value
	if (e.currentTarget.checked){
		if (window.filter_command.trim() == "") {
			type("filter " + this.value, "command", 3, false, true, false)
		}
		else {
			if (container.innerHTML.trim() == "") {
				type(window.filter_command + " " + this.value, "command", 3, true, true, true)
			}
			else {
				type(" " + this.value, "command", 3, true, true, true)
			}
		}
	}
	//remove filter this.value
	else {
		// if the command is empty right now, then retype the full command updated
		if (container.innerHTML.trim() == ""){
			window.filter_command = window.filter_command.replace(" " + this.value, '');
			if (window.filter_command == "filter"){	// if there is no more filters active then avoid to print the command
				window.filter_command = "";
				return;
			}
			type(window.filter_command, "command", 3, false, false, false)
		}
		// else remove character by character the filter to be removed
		else {
			let start_index = window.filter_command.indexOf(" " + this.value);
			let end_index = this.value.length;
			window.filter_command = window.filter_command.replace(" " + this.value, '');
			if (window.filter_command == "filter") {// if there is no more filters active then delete every character in the command
				start_index = 0;
				end_index += window.filter_command.length;
				window.filter_command = "";
			}
			let j = 0;
			interval = 30;
			for (let i = end_index; i >= 0; i--) {
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


