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
	let command_field = document.getElementById("command");
	let expression_counter = document.getElementById("expression_counter");
	for (let i = 0; i < expressions_content.length; i++) {
		if (!expressions_content[i].toLowerCase().includes(inputValue.toLowerCase())) {	//keeps only the string that includes the user input string
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

		arg_link.addEventListener("mouseover", function() {
			//if the command is empty then type also "inspect "
			if (command_field.innerHTML.trim() == "") {
				window.filter_command = "inspect \"" + this.innerHTML + "\"";
				type("inspect \"" + this.innerHTML + "\"", "command", 4, false, false, false);
			}
			else {
				//if the command is already correct do nothing, otherwire replace only what inside the double quote
				if (window.filter_command != "inspect \"" + this.innerHTML + "\""){
					killTimers();
					command_field.innerHTML = "inspect ";
					window.filter_command = "inspect \"" + this.innerHTML + "\"";
					type("\"" + this.innerHTML + "\"", "command", 4, true, false, false);
				}
			}
		})
	}
	
	if (html_list.childElementCount == 1) {
		expression_counter.innerHTML = "1 expression found";
	}
	else if (html_list.childElementCount == 0) {
		expression_counter.innerHTML = "No expressions found";
	}
	else {
		expression_counter.innerHTML = html_list.childElementCount + " expressions found";
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
	let search_field = document.getElementById("expression_name");
	search_field.addEventListener("input", function() {
		updateResults(this.value);
	})
}


// make the width of the container fixed once is determined
function set_list_size() {
	let container = document.getElementById("expression_list");
	let currentWidth = container.getBoundingClientRect();
	container.style.width = parseInt(currentWidth.width)+1 + "px";
	console.log(currentWidth.width+1 + "px")
}