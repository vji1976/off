#!/usr/bin/env python3
"""OFFICE TOOLKIT v1.0

CODED ON:
	04.19.2020
CODED BY:
	MosesLawn
CODE ENV:
	python 3.7 win10x64 Geany
GITHUB:
	https://github.com/vji1976/off.git
DEPENDENCIES:
	pip install Pillow
	pip install tkcalendar
	pip install python-docx
	pip install selenium
	pip install beautifulsoup4
"""
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.iconbitmap("img/favicon.ico")
		self.title("Office ToolKit 1.0")
		
	def drawmenu(self):
		pass
		
	def drawgui(self):
		pass
		
	def drawstatus(self):
		pass
		
if __name__ == '__main__':
	root = App()
	root.geometry("800x600+200+200")
	root.minsize(800,600)
	root.mainloop()
