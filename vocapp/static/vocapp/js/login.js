var old_username = null;
var old_password_len = null;
var password_changed = false;

var speed = 3;

function hideErrorMessage() {
	let error_message = document.getElementsByClassName("error_message")[0];
	if (error_message) {
		error_message.style.display = "none";
	}
}

function addLoginEvent() {
	let submit_button = document.getElementById("submit_login");
	submit_button.addEventListener("mouseover", update_login_shell)
	submit_button.addEventListener("click", function(){
		speed = 5;
		update_login_shell();
	})
	let password_input = document.getElementById("id_password");
	password_input.addEventListener("input", function() {
		password_changed = true;
	})
}

async function update_login_shell(e) {
	let username = document.getElementById("id_username").value.trim();
	let password_len = document.getElementById("id_password").value.length;
	let command_container = document.getElementById("command");
	if (old_username == null || command_container.innerHTML.trim() == "") {
		type("login -u -p " + username + " " + "*".repeat(password_len), "command", speed, false, false, false);
	}
	else if (old_username != username) {
		while (window.active_timers > 0){
			await new Promise(r => setTimeout(r, 20));
		}
		command_container.innerHTML = command_container.innerHTML.substring(0, "login -u -p ".length);
		type(username + " " + "*".repeat(password_len), "command", speed, true, false, true);
	}
	else if (password_changed) {
		while (window.active_timers > 0){
			await new Promise(r => setTimeout(r, 20));
		}
		command_container.innerHTML = command_container.innerHTML.substring(0, command_container.innerHTML.length - old_password_len);
		type("*".repeat(password_len), "command", speed, true, false, true);
	}
	old_username = username;
	old_password_len = password_len;
	password_changed = false;
}
