import eel
import segments



segment_types = {
	"plain text":segments.plain,
	"colored text":None,
	"rainbow text":None,
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
	return "success"



@eel.expose
def new_segment(index):
	global message
	global segment_types
	message.append(list(segment_types.values())[index])
	print(message)



eel.init("web")
eel.start("main.html")