class plain:
	def __init__(self):
		self.text = ""
		self.html = """<textarea id="segment_text"></textarea>"""

	def get_preview(self):
		return self.text

	def get_result(self):
		return self.text