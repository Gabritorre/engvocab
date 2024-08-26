function toggle_report_form() {
	let report_form = document.getElementsByClassName("report_form")[0];
	if (report_form.classList.contains("hidden_object")) {
		report_form.classList.remove("hidden_object");
		report_form.classList.add("visible_object");
	}
	else {
		report_form.classList.remove("visible_object");
		report_form.classList.add("hidden_object");
	}
	let img_button = document.getElementById("report_button").children[0];
	if (img_button.src.includes("down")) {
		img_button.src = img_button.src.replace("down", "up");
	}
	else {
		img_button.src = img_button.src.replace("up", "down");
	}
}

function check_report_form(e) {
	const checkboxes = document.querySelectorAll('.report_form input[type="checkbox"]');
	let checked = false;
	
	for (let i = 0; i < checkboxes.length; i++) {
		if (checkboxes[i].checked) {
			checked = true;
			break;
		}
	}
	
	if (!checked) {
		alert('Select at least one option.');
		e.preventDefault();
	}
}

function add_report_events() {
	const report_button = document.getElementById("submit_report_button");
	report_button.addEventListener("mouseover", function() {
		type("send_report", "command", 4, false, false, false);
	})
	report_button.addEventListener("mouseout", clear_command);
}