import colorsys



def rgb_to_hex(rgb):
	return "#%02x%02x%02x" % rgb

def hex_to_rgb(hex):
	return tuple(int(hex.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

black = "#000000"



class plain:
	def __init__(self):
		self.text = ""
		self.base_html = """<p>plain text</p>
				<textarea id="text" class="input" style="width:300px;">{}</textarea>"""

	def get_html(self):
		return self.base_html.format(self.text)

	def get_preview(self):
		return self.text

	def get_result(self):
		return self.text



class color:
	def __init__(self):
		self.text = ""
		self.color = black
		self.base_html = """<p>colored text</p>
				<textarea id="text" class="input" style="width:300px;">{0}</textarea>
				<input type="color" id="color" class="input" value="{1}"></input>"""
		self.preview_html = """<span style="color:{1};">{0}</span>"""

	def get_html(self):
		return self.base_html.format(self.text, self.color)

	def get_preview(self):
		return self.preview_html.format(self.text, self.color)

	def get_result(self):
		return "[c/{0}:{1}]".format(self.color[1:], self.text)



class rainbow:
	def __init__(self):
		self.text = ""
		self.color = black
		self.offset = 0
		self.base_html = """<p>rainbow text</p>
				<textarea id="text" class="input" style="width:300px;">{0}</textarea>
				<input type="color" id="color" class="input" value="{1}"></input>
				<input type="number" id="offset" class="input" value="{2}"></input>"""
		self.preview_letter_html = """<span style="color:{1};">{0}</span>"""

	def get_html(self):
		return self.base_html.format(self.text, self.color, self.offset)

	def get_preview(self):
		rgb_color = self.color
		color = colorsys.rgb_to_hsv(*(channel/255 for channel in hex_to_rgb(rgb_color)))
		preview = ""
		for letter in self.text:
			rgb_color = rgb_to_hex(tuple([int(channel*255) for channel in colorsys.hsv_to_rgb(*color)]))
			letter = self.preview_letter_html.format(letter, rgb_color)
			preview += letter
			color = tuple([color[0] + int(self.offset) / 360, color[1], color[2]])
		return preview

	def get_result(self):
		rgb_color = self.color
		color = colorsys.rgb_to_hsv(*(channel/255 for channel in hex_to_rgb(rgb_color)))
		result = ""
		for letter in self.text:
			rgb_color = rgb_to_hex(tuple([int(channel*255) for channel in colorsys.hsv_to_rgb(*color)]))
			letter = "[c/{0}:{1}]".format(rgb_color[1:], letter)
			result += letter
			color = tuple([color[0] + int(self.offset) / 255, color[1], color[2]])
		return result