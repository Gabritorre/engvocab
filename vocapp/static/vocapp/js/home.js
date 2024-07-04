function show_solution() {
	let show_button = document.getElementById("show_button");
	let solution_div = document.getElementById("hidden_solution");
	show_button.hidden = true;
	solution_div.removeAttribute("hidden")
	solution_div.classList.add("solution");
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