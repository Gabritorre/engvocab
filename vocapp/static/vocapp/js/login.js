var old_username = null;
var old_password_len = null;
var password_changed = false;

function addLoginEvent() {
	let submit_button = document.getElementById("submit_login");
	submit_button.addEventListener("mouseover", update_login_shell)
	submit_button.addEventListener("click", update_login_shell)
	let password_input = document.getElementById("id_password");
	password_input.addEventListener("input", function() {
		password_changed = true;
	})
}

async function update_login_shell(e) {
	let username = document.getElementById("id_username").value.trim();
	let password_len = document.getElementById("id_password").value.length;
	let command_container = document.getElementById("command");
	console.log("user: " + username + " pass_len: " + password_len);
	if (old_username == null || command_container.innerHTML.trim() == "") {
		old_username = username;
		old_password_len = password_len;
		type("login -u -p " + username + " " + "*".repeat(password_len), "command", 3, false, false, false);
	}
	else if (old_username != username) {
		while (window.active_timers > 0){
			await new Promise(r => setTimeout(r, 20));
		}
		command_container.innerHTML = command_container.innerHTML.substring(0, "login -u -p ".length);
		type(username + " " + "*".repeat(password_len), "command", 3, true, false, true);
		old_username = username;
		old_password_len = password_len;
		password_changed = false;
	}
	else if (password_changed) {
		while (window.active_timers > 0){
			await new Promise(r => setTimeout(r, 20));
		}
		command_container.innerHTML = command_container.innerHTML.substring(0, command_container.innerHTML.length - old_password_len);
		type("*".repeat(password_len), "command", 3, true, false, true);
		old_password_len = password_len;
		password_changed = false;
	}
}
