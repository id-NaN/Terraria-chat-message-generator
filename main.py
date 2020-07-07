import json
import os
import colorsys
import colr
import pyperclip
import eel



def number_place_minimum(number, places):
	return (places - len(number)) * "0" + number



eel.init("web")
eel.start("main.html")