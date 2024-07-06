function show_solution() {
	let show_button = document.getElementById("show_button");
	let solution_div = document.getElementById("solution");
	show_button.classList.remove("visible_object");
	show_button.classList.add("hidden_object");
	
	solution_div.classList.remove("hidden_object");
	solution_div.classList.add("visible_object");
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