var old_username = null;
var old_password1_len = null;
var old_password2_len = null;
var password1_changed = false;
var password2_changed = false;

var speed = 4

function addSignupEvent() {
	let submit_button = document.getElementById("submit_signup");
	submit_button.addEventListener("mouseover", update_signup_shell)
	submit_button.addEventListener("click", function(){
		speed = 5;
		update_signup_shell();
	})
	let password1_input = document.getElementById("id_password1");
	password1_input.addEventListener("input", function() {
		password1_changed = true;
	})
	let password2_input = document.getElementById("id_password2");
	password2_input.addEventListener("input", function() {
		password2_changed = true;
	})
}

async function update_signup_shell(e) {
	let username = document.getElementById("id_username").value.trim();
	let password1_len = document.getElementById("id_password1").value.length;
	let password2_len = document.getElementById("id_password2").value.length;
	let command_container = document.getElementById("command");
	if (old_username == null || command_container.innerHTML.trim() == "") {
		type("signup -u -p " + username + " " + "*".repeat(password1_len) + " " + "*".repeat(password2_len), "command", speed, false, false, false);
	}
	else if (old_username != username) {
		while (window.active_timers > 0){
			await new Promise(r => setTimeout(r, 20));
		}
		command_container.innerHTML = command_container.innerHTML.substring(0, "signup -u -p ".length);
		type(username + " " + "*".repeat(password1_len) + " " + "*".repeat(password2_len), "command", speed, true, false, true);
	}
	else if (password1_changed) {
		while (window.active_timers > 0){
			await new Promise(r => setTimeout(r, 20));
		}
		command_container.innerHTML = command_container.innerHTML.substring(0, command_container.innerHTML.length - old_password1_len - old_password2_len - 1);
		type("*".repeat(password1_len) + " " + "*".repeat(password2_len), "command", speed, true, false, true);
	}
	else if (password2_changed) {
		while (window.active_timers > 0){
			await new Promise(r => setTimeout(r, 20));
		}
		command_container.innerHTML = command_container.innerHTML.substring(0, command_container.innerHTML.length - old_password2_len);
		type("*".repeat(password2_len), "command", speed, true, false, true);
	}
	old_username = username;
	old_password1_len = password1_len;
	old_password2_len = password2_len
	password1_changed = false;
	password2_changed = false;
}
