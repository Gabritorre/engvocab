
function updateResults(expressions_list, inputValue) {
	expressions_list = JSON.parse(expressions_list);
	let expressions_dict = {};
	for (const[key, value] of Object.entries(expressions_list)){
		expressions_dict[key] = value;
	}
	values = Object.values(expressions_list);
	values.sort();
	clear_expressions();

	let html_list = document.getElementById("expressions");
	for (let i = 0; i < values.length; i++){
		if (!values[i].includes(inputValue)) {
			continue;
		}
		let arg_link = document.createElement("a");
		var link_text = document.createTextNode(values[i]);
		let elem = document.createElement("li");
		arg_link.appendChild(link_text);
		arg_link.href = "expression/" + Object.keys(expressions_dict).find(key => expressions_dict[key] === values[i]);
		elem.appendChild(arg_link);
		html_list.append(elem);
	}
}

function clear_expressions(){
	try{
		let delete_list = document.getElementById("expressions");
		while (delete_list.firstChild) {
			delete_list.removeChild(delete_list.lastChild);
		}
	}catch(e){}
}
