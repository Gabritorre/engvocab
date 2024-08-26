function show_solution() {
	let show_button = document.getElementById("show_button");
	let solution_div = document.getElementById("solution");
	show_button.classList.remove("visible_object");
	show_button.classList.add("hidden_object");
	
	solution_div.classList.remove("hidden_object");
	solution_div.classList.add("visible_object");
}

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

function filters_button_style() {
	let filters = document.getElementsByClassName("filter");
	for (let i = 0; i < filters.length; i++) {
		filters[i].children[0].addEventListener("change", function(event) {
			if (event.currentTarget.checked) {
				filters[i].children[1].classList.add("filter_on");
			}
			else {
				filters[i].children[1].classList.remove("filter_on");
			}
		});
	}
}
