import json
import os
import colorsys
import colr
import pyperclip
import eel



eel.init("web")
eel.start("main.html")


def clear():
	os.system("cls")



def y_n_input(string = "", clear_screen = True):
	if clear_screen:
		clear()
	while True:
		try:
			return bool(int(input(string + "(y/n)").replace("y", "1").replace("n", "0")))
		except:
			clear()
			print("invalid input")



def choice_input(string = "", possibilities = [], clear_screen = True):
	if clear_screen:
		clear()
	if possibilities == []:
		return None
	while True:
		input_string = input(string + "(" + "/".join(possibilities) + ")")
		if input_string in possibilities:
			clear()
			return input_string
		else:
			clear()
			print("invalid input")



def number_place_minimum(number, places):
	return (places - len(number)) * "0" + number



class Item:
	def __init__(self, dictionary):
		[setattr(self, key, value) for key, value in dictionary.items()]

	def __str__(self):
		return "\n".join([
				"id:" + "\t" * 2 + str(self.item_id),
				"name:" + "\t" + self.item_name,
				"wiki:" + "\t" + self.wiki_url
				])



class NewMessage:
	def __init__(self):
		self.elements = []
		self.preview_elements = []

	def __str__(self):
		return "".join(self.elements)

	def color_segment(self):
		color_system = choice_input("which color system should be used?",("rgb", "hsv"))
		adjust_color = True
		while adjust_color:
			while True:
				try:
					raw_color = [float(int(channel)) for channel in input("please enter a color inside your color system of choice:\n").split()]
					if len(raw_color) == 3:
						break
				except:
					pass
				print("invalid input")
			if color_system == "hsv":
				color = (raw_color[0] / 360, raw_color[1] / 100, raw_color[2] / 100)
				color_rgb = [int(c * 255) for c in colorsys.hsv_to_rgb(color[0], color[1], color[2])]
			else:
				color_rgb = [int(c) for c in raw_color]
			preview = colr.color("██", fore = color_rgb)
			print(preview)
			adjust_color = y_n_input("Do you want to adjust the color?", False)
			clear()
		adjust_text = True
		while adjust_text:
			print(preview)
			text = input("enter the text: ")
			text_preview = colr.color(text, fore = color_rgb)
			clear()
			print(text_preview)
			adjust_text = y_n_input("Do you want to adjust the text?", False)
			clear()
		color_hex = "".join([number_place_minimum(hex(c)[2:], 2) for c in color_rgb])
		segment = "[c/" + color_hex + ":" + text + "]"
		self.elements.append(segment)
		self.preview_elements.append(text_preview)


	def rainbow_segment(self):
		confirmed = False
		adjust_text = True
		while adjust_text:
			text = input("enter the text: ")
			clear()
			print()
			adjust_text = y_n_input(text + "\nDo you want to adjust the text?")
			clear()
		while not confirmed:
			while True:
				try:
					raw_color = [float(int(channel)) for channel in input("please enter a color to start the rainbow at:\n").split()]
					if len(raw_color) == 3:
						break
				except:
					pass
				print("invalid input")
			while True:
				try:
					offset = int(input("enter the offset for the rainbow effect "))
					break
				except:
					pass
				clear()
				print("invalid input")
			clear()
			segment = ""
			preview = ""
			for character in text:
				color = (raw_color[0] / 360, raw_color[1] / 100, raw_color[2] / 100)
				color_rgb = [int(c * 255) for c in colorsys.hsv_to_rgb(color[0], color[1], color[2])]
				preview += colr.color(character, fore = color_rgb)
				color_hex = "".join([number_place_minimum(hex(c)[2:], 2) for c in color_rgb])
				character = "[c/" + color_hex + ":" + character + "]"
				segment += character
				raw_color[0] += offset
			confirmed = y_n_input(preview + "\ndoes that look right?")
		self.elements.append(segment)
		self.preview_elements.append(preview)




	def build(self):
		while True:
			clear()
			input_string = choice_input(
				"\n".join(
					(
						"".join(self.preview_elements),
						"What should be done?",
						"add colored text(c)",
						"add rainbow effect text(r)",
						"remove last element(l)",
						"copy message(m)",
						"exit(e)"
					)
				) + "\n",
			("c", "r", "l", "m", "e"),
			False)
	
			if input_string == "c":
				self.color_segment()
			elif input_string == "r":
				self.rainbow_segment()
			elif input_string == "l":
				if y_n_input("are you sure you want to delete " + self.preview_elements[-1]):
					del self.elements[-1]
					del self.preview_elements[-1]
			elif input_string == "m":
				message_string = "".join(self.elements)
				pyperclip.copy(message_string)
				input(message_string)
			elif input_string == "e":
				return



with open("C:\\Users\\morga\\Desktop\\Projects\\terraria chat generator\\terraria_items.json", "r") as items_raw:
	items_list = json.load(items_raw)
items = [Item(dictionary) for dictionary in items_list]
del items_raw
del items_list



clear()
message = NewMessage()
message.build()
input(message)