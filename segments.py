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