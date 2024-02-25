
function updateResults(expressions_list, inputValue) {
	var expressions_list = JSON.parse(expressions_list);
	for(i = 0; i < expressions_list.length; i++){
		console.log(expressions_list[i])
	};
	document.getElementById('results').textContent = "Searching for: " + inputValue;
}
