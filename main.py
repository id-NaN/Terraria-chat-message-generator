import eel
import segments



segment_types = {
	"plain text":segments.plain,
	"colored text":segments.color,
	"rainbow text":segments.rainbow,
}
print(list(segment_types.keys()))


def number_place_minimum(number, places):
	return (places - len(number)) * "0" + number



class Segment:
	def __init__(self):
		self.type = None



@eel.expose
def get_start_data():
	global segment_types
	data = {
	"segment_types":(list(segment_types.keys()))
	}
	return data



message = []
@eel.expose
def reset_editor():
	global message
	message = []
	print("reset")
	eel.update_segment_display([])
	return "success"



@eel.expose
def new_segment(index):
	global message
	global segment_types
	message.append(list(segment_types.values())[index]())
	print(message)
	message_preview = "".join([segment.get_preview() for segment in message])
	message_result = "".join([segment.get_result() for segment in message])

	eel.update_segment_display([s.get_html() for s in message])



@eel.expose
def update(keys, values):
	global message
	print(keys, "\n" ,values)
	for outer_index, segment_keys in enumerate(keys):
		print()
		segment_values = values[outer_index]
		for inner_index, key in enumerate(segment_keys):
			value = segment_values[inner_index]
			print(key, value)
			setattr(message[outer_index], key, value)
	message_preview = "".join([segment.get_preview() for segment in message])
	message_result = "".join([segment.get_result() for segment in message])
	eel.update_results(message_preview, message_result)



eel.init("web")
eel.start("main.html", size = (1000, 650))