import json
import os
import colorsys
import colr
import pyperclip
import eel



eel.init("web")
eel.start("main.html")



def number_place_minimum(number, places):
	return (places - len(number)) * "0" + number



# class Item:
# 	def __init__(self, dictionary):
# 		[setattr(self, key, value) for key, value in dictionary.items()]

# 	def __str__(self):
# 		return "\n".join([
# 				"id:" + "\t" * 2 + str(self.item_id),
# 				"name:" + "\t" + self.item_name,
# 				"wiki:" + "\t" + self.wiki_url
# 				])



# with open("C:\\Users\\morga\\Desktop\\Projects\\terraria chat generator\\terraria_items.json", "r") as items_raw:
# 	items_list = json.load(items_raw)
# items = [Item(dictionary) for dictionary in items_list]
# del items_raw
# del items_list