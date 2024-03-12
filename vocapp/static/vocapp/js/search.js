
function updateResults(expressions_list, inputValue) {
	expressions_list = JSON.parse(expressions_list);
	let html_list = document.getElementById("expressions");
	for (const [key, value] of Object.entries(expressions_list)){
		if (!value.includes(inputValue)) {
			continue;
		}
		let arg_link = document.createElement("a");
		var link_text = document.createTextNode(value);
		let elem = document.createElement("li");
		arg_link.appendChild(link_text);
		arg_link.href = "expression/" + key;
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
