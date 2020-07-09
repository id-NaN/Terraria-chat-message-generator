import eel
import segments



segment_types = {
	"plain text":segments.plain,
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
	eel.update_segment_display([s.get_html() for s in message])



eel.init("web")
eel.start("main.html")