var expressions_dict;
var expressions_content;

// get a json string 'expressions_list' that will be parsed in a JSON object.
//save in a dictionary the key value pair 'id_expression:content'
//save in a array only the content
//sort the content array
function sortExpressions(expressions_list) {
	expressions_list = JSON.parse(expressions_list);
	expressions_dict = {};
	for (const[key, value] of Object.entries(expressions_list)){
		expressions_dict[key] = value;
	}
	expressions_content = Object.values(expressions_list);
	expressions_content.sort();
}

//update the search output every time the user press a key
function updateResults(inputValue) {
	clearExpressions();

	let html_list = document.getElementById("expressions");
	for (let i = 0; i < expressions_content.length; i++) {
		if (!expressions_content[i].includes(inputValue)) {	//keeps only the string that includes the user input string
			continue;
		}
		let arg_link = document.createElement("a");
		var link_text = document.createTextNode(expressions_content[i]);
		let elem = document.createElement("li");
		arg_link.appendChild(link_text);
		//get the ID of the current expression to build the url
		arg_link.href = "expression/" + Object.keys(expressions_dict).find(key => expressions_dict[key] === expressions_content[i]);
		elem.appendChild(arg_link);
		html_list.append(elem);
	}
}

//clear the search output
function clearExpressions(){
	try{
		let delete_list = document.getElementById("expressions");
		while (delete_list.firstChild) {
			delete_list.removeChild(delete_list.lastChild);
		}
	}catch(e){}
}

function addSearchEvent() {
	let apply_button = document.getElementById("expression_name");
	apply_button.addEventListener("input", function() {
		updateResults(this.value);
	})
	apply_button.addEventListener("focus", function() {
		type("find ", "command", 3, false, false, false);
	})
	apply_button.addEventListener("focusout", function() {
		clear_command();
	})
}