function show_solution() {
	let show_button = document.getElementById("show_button");
	let solution_div = document.getElementById("hidden_solution");
	show_button.hidden = true;
	solution_div.removeAttribute("hidden")
	solution_div.classList.add("solution");
}