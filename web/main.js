async function load_data() {
	let response = await eel.get_start_data()();
	let segment_types = response.segment_types;
	let dropdown_content = "";
	
	for (var i = 0; i <= segment_types.length - 1; i++) {
		let segment_type = segment_types[i];
		dropdown_content += "<a onclick=\"eel.new_segment(" + i + ")\" class=\"unselectable\">" + segment_type + "</a>"
	}



	let dropdown = document.querySelectorAll("#select_segment_dropdown .dropdown_content");
	dropdown[0].innerHTML = dropdown_content;
	console.log(dropdown_content);
}



eel.expose(update_segment_display)
function update_segment_display(segments, message_preview, message_result) {
	let segment_html = "";
	for (var i = 0; i < segments.length; i++) {
		segment = segments[i];
		segment_html +=
			"<div class=\"segment_container\">" + segment + "</div>"
	}
	let container = document.getElementById("main_segment_container");
	container.innerHTML = segment_html;
	for (var i = container.children.length - 1; i >= 0; i--) {
		child = container.children[i];
		child.setAttribute("onchange", "process_data()");
	}

	document.getElementById("preview_area").innerHTML = message_preview
	document.getElementById("result_area").innerHTML = message_result
}



function process_data() {
	let main_container = document.getElementById("main_segment_container");
	let keys = [];
	let values = [];

	for (var i = 0; i <= main_container.children.length - 1; i++) {
		let container = main_container.children[i];
		keys.push([]);
		values.push([]);

		for (var j = 0; j <= container.children.length - 1; j++) {
			let child = container.children[j];
			if (child.classList.contains("input")) {
				keys[i].push(child.id);
				values[i].push(child.value);
			}
		}
	}
	eel.update(keys, values);
}