from tkinter import * 
from tkinter import ttk  
from tkinter.filedialog import *

from backend import *
from PIL import Image, ImageTk

import os

from backend import *


class ImageFilter(Tk):
	def __init__(self):
		Tk.__init__(self)

		self.geometry("900x900")
		self.choose = Button(self, text = "Choose Photo", command = self.on_choose)
		self.save = Button(self, text = "Save",  width=10, command = self.on_save)
		self.F1 = Button(self, width=15, height=2, text = "F1", command = self.on_F1)
		self.F2 = Button(self, width=15, height=2, text = "F2", command = self.on_F2)
		self.F3 = Button(self, width=15, height=2, text = "F3", command = self.on_F3)
		self.F4 = Button(self, width=15, height=2, text = "F4", command = self.on_F4)
		self.photo_label = Label(self, image=None)

		self.choose.grid(column = 0, row = 0)
		self.save.grid(column = 0, row = 1)
		self.F1.grid(column = 2, row = 3)
		self.F2.grid(column = 3, row = 3)
		self.F3.grid(column = 2, row = 4)
		self.F4.grid(column = 3, row = 4)
		self.photo_label.grid(column=2, row=0, columnspan=5, rowspan=3)
	
		
	def on_choose(self):
		self.from_dir = askopenfilename()
		print(self.from_dir)
		self.image = Image.open(self.from_dir)
		print(self.image)
		photo = ImageTk.PhotoImage(self.image)
		
		self.photo_label.configure(image=photo)
		self.photo_label.image = photo
		
		self.photo_label.grid(column=2, row=0, columnspan=5, rowspan=3)

	def on_F1(self):
		self.filter_image = filter1(self.image)
		self.img = ImageTk.PhotoImage(self.filter_image)

		self.photo_label.configure(image=self.img)
		self.photo_label.image = self.img

		self.photo_label.grid(column=2, row=0, columnspan=5, rowspan=3)

	def on_F2(self):
		self.filter_image = filter2(self.image)
		self.img = ImageTk.PhotoImage(self.filter_image)
		self.photo_label.configure(image=self.img)
		self.photo_label.image = self.img

		self.photo_label.grid(column=2, row=0, columnspan=5, rowspan=3)


	def on_F3(self):
		self.filter_image = filter3(self.image)
		self.img = ImageTk.PhotoImage(self.filter_image)
		self.photo_label.configure(image=self.img)
		self.photo_label.image = self.img

		self.photo_label.grid(column=2, row=0, columnspan=5, rowspan=3)

	def on_F4(self):
		self.filter_image = filter4(self.image)
		self.img = ImageTk.PhotoImage(self.filter_image)
		self.photo_label.configure(image=self.img)
		self.photo_label.image = self.img

		self.photo_label.grid(column=2, row=0, columnspan=5, rowspan=3)

	def on_save(self):
		self.filter_image.save("doggy.png")


app = ImageFilter()
app.mainloop()