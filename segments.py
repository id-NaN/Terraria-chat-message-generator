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
		self.color = ""
		self.base_html = """<p>colored text</p>
				<textarea id="text" class="input" style="width:300px;">{0}</textarea>
				<input type="color" id="color" class="input" value="{1}"></input>"""

	def get_html(self):
		return self.base_html.format(self.text, self.color)

	def get_preview(self):
		return self.text

	def get_result(self):
		return "[c/{0}:{1}]".format(self.color[1:], self.text)