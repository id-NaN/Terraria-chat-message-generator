async function reset_message() {
	console.log("resetting...");
	let response = await eel.reset_editor()();
	console.log(response);
}
async function load_data(argument) {
	let response = await eel.get_start_data()();
	let segment_types = response.segment_types;
	let dropdown_content = "";
	for (var i = 0; i <= segment_types.length - 1; i++) {
		let segment_type = segment_types[i];
		dropdown_content += "<a onclick=\"eel.new_segment(" + i + ")\">" + segment_type + "</a>"
	}
	let dropdown = document.querySelectorAll("#select_segment_dropdown .dropdown_content")
	dropdown[0].innerHTML = dropdown_content
	console.log(dropdown_content);
}