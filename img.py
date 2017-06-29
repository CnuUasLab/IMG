import numpy as np
import cv2
import Tkinter as tk
from Tkinter import Label, Entry, Button
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from PIL import Image, ImageTk
import glob
import sys
from enum import Enum
from button_press import key_press, mouse_press, mouse_release
from image_object import img_obj as img_obj
from var import mode
import os

imgW = 1200
imgH = 800

nullImg = np.zeros((1,1,3), np.uint8)

fontEntrySize = 20
fontLabelSize = 16
fontType = "Courier"

class img:

	def __init__(self):
		self.cropList = []
		self.origList = []
		self.origIndex = -1
		self.cropIndex = 0
		self.imageModified = False
		# self.mode = imageType.original
		self.mode = mode.orig
		self.index = -1
		self.numOrig = 0
		self.pt0 = 0,0
		self.pt1 = 0,0
		self.pts = []
		self.imgW = imgW
		self.imgH = imgH
		self.orienVals = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
		self.shapeVals = ["circle", "semicircle", "quarter_circle", "triangle",
		"square", "rectangle", "trapezoid", "pentagon", "hexagon", "heptagon",
		"octagon", "star", "cross"]
		self.colorVals = ["white", "black", "gray", "red", "blue", "green", "yellow",
		"purple", "brown", "orange"]

		# null obj
		self.currImgObj = img_obj(self, nullImg)

		self.import_images()

		#Set up GUI
		self.window = tk.Tk()  #Makes main window
		self.setup_GUI()

	def import_images(self):
		for filename in glob.glob('SampleImages/*.jpg'):
			img = cv2.imread(filename)
			img = cv2.resize(img, (imgW, imgH))
			image_obj = img_obj(self, img)

			self.origList.append(image_obj)
			self.numOrig = self.numOrig + 1

			print "image imported",filename

		if self.numOrig > 0 and self.origIndex < 0:
			self.origIndex = 0
		self.update_curr_img_obj()

	def import_images_alt(self):
		# *******************************************************
		#
		# uncomment this line to clear the list of images on open
		# 
		# *******************************************************
		# self.origList = []
		path = tkFileDialog.askdirectory()
		if os.path.exists(path):
			path += '/*.jpg'
			for filename in glob.glob(path):
				img = cv2.imread(filename)
				img = cv2.resize(img, (imgW, imgH))
				image_obj = img_obj(self, img)

				self.origList.append(image_obj)
				self.numOrig = self.numOrig + 1

				print "image imported",filename

			if self.numOrig > 0 and self.origIndex < 0:
				self.origIndex = 0
			self.update_curr_img_obj()
		else:
			print "path does not exist, opening default dir"
			self.import_images()

	def setup_GUI(self):
		self.window.wm_title("Image Manipulation Genie (IMG)")
		self.window.config(background="#FFFFFF")

		#Graphics window
		self.imageFrame = tk.Frame(self.window, width=imgW, height=imgH)
		self.imageFrame.grid(row=0, column=0, padx=10, pady=2)

		self.lmain = tk.Label(self.imageFrame)
		self.lmain.grid(row=0, column=0)

		self.image_loop() # display image function

		# bind the following three to the main loop
		self.window.bind_all('<KeyPress>', lambda event: key_press(event, self, self.currImgObj))
		self.window.bind_all('<ButtonPress-1>', lambda event: mouse_press(event, self, self.currImgObj))
		self.window.bind_all('<ButtonRelease-1>', lambda event: mouse_release(event, self, self.currImgObj))

		# run the main loop of tkinter
		self.window.mainloop() #Starts GUI

	def image_loop(self):
		self.show_image()
		#self.lmain.after(100, lambda: self.lmain.focus_force())
		self.lmain.after(250, self.image_loop)

	def show_image(self):
		self.update_curr_img_obj()
		liveImage = self.currImgObj.get_image_live()
		cv2image = cv2.cvtColor(liveImage, cv2.COLOR_BGR2RGBA)
		tempImage = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=tempImage)
		self.lmain.imgtk = imgtk
		self.lmain.configure(image=imgtk)

	def setup_mode(self):
		if self.mode == mode.orig:
			self.sliderFrame.grid_forget()
			self.window.geometry("")
		else:
			#Slider window (slider controls stage position)
			self.sliderFrame = tk.Frame(self.window, width=800, height=400)
			self.sliderFrame.grid(row = 1, column=0, padx=10, pady=2)
			self.sliderFrame.config(background="#FFFFFF")
			Label(self.sliderFrame, text="Type".rjust(20), font=(fontType, fontLabelSize)).grid(row=1, column=1)
			Label(self.sliderFrame, text="Latitude".rjust(20), font=(fontType, fontLabelSize)).grid(row=2, column=1)
			Label(self.sliderFrame, text="Longitude".rjust(20), font=(fontType, fontLabelSize)).grid(row=3, column=1)
			Label(self.sliderFrame, text="Orientation".rjust(20), font=(fontType, fontLabelSize)).grid(row=4, column=1)
			Label(self.sliderFrame, text="Shape".rjust(20), font=(fontType, fontLabelSize)).grid(row=5, column=1)
			Label(self.sliderFrame, text="Background Color".rjust(20), font=(fontType, fontLabelSize)).grid(row=6, column=1)
			Label(self.sliderFrame, text="Alphanumeric".rjust(20), font=(fontType, fontLabelSize)).grid(row=7, column=1)
			Label(self.sliderFrame, text="Alphanumeric Color".rjust(20), font=(fontType, fontLabelSize)).grid(row=8, column=1)
			Label(self.sliderFrame, text="Description".rjust(20), font=(fontType, fontLabelSize)).grid(row=9, column=1)

			self.orientationValue = tk.StringVar(self.sliderFrame)
			self.orientationValue.set("N")
			self.shapeValue = tk.StringVar(self.sliderFrame)
			self.shapeValue.set("circle")
			self.bkColorValue = tk.StringVar(self.sliderFrame)
			self.bkColorValue.set("white")
			self.alphaColorValue = tk.StringVar(self.sliderFrame)
			self.alphaColorValue.set("white")

			self.entryType = Entry(self.sliderFrame)
			self.entryLat = Entry(self.sliderFrame)
			self.entryLong = Entry(self.sliderFrame)
			self.optionOrien = tk.OptionMenu(self.sliderFrame, self.orientationValue, *self.orienVals)
			self.optionShape = tk.OptionMenu(self.sliderFrame, self.shapeValue, *self.shapeVals)
			self.optionBkColor = tk.OptionMenu(self.sliderFrame, self.bkColorValue, *self.colorVals)
			self.entryAlpha = Entry(self.sliderFrame)
			self.optionAlphaColor = tk.OptionMenu(self.sliderFrame, self.alphaColorValue, *self.colorVals)
			self.entryDesc = Entry(self.sliderFrame)
			self.entryRF = Button(self.sliderFrame, text="Return Focus", command=self.return_focus)

			self.entryType.grid(row=1, column=2)
			self.entryLat.grid(row=2, column=2)
			self.entryLong.grid(row=3, column=2)
			self.optionOrien.grid(row=4, column=2)
			self.optionShape.grid(row=5, column=2)
			self.optionBkColor.grid(row=6, column=2)
			self.entryAlpha.grid(row=7, column=2)
			self.optionAlphaColor.grid(row=8, column=2)
			self.entryDesc.grid(row=9, column=2)
			self.entryRF.grid(row=10, column=2)

			self.entryType.config(font=(fontType, fontEntrySize))
			self.entryLat.config(font=(fontType, fontEntrySize))
			self.entryLong.config(font=(fontType, fontEntrySize))
			self.optionOrien.config(font=(fontType, fontEntrySize))
			self.optionShape.config(font=(fontType, fontEntrySize))
			self.optionBkColor.config(font=(fontType, fontEntrySize))
			self.entryAlpha.config(font=(fontType, fontEntrySize))
			self.optionAlphaColor.config(font=(fontType, fontEntrySize))
			self.entryDesc.config(font=(fontType, fontEntrySize))
			self.entryRF.config(font=(fontType, fontEntrySize))

	def return_focus(self):
		self.currImgObj.get_entry_data()
		self.window.focus_force()
		print "focus returned."

	def update_curr_img_obj(self):
		if len(self.origList) and self.mode == mode.orig:
			self.currImgObj = (self.origList[self.origIndex])
		elif len(self.cropList) and self.mode == mode.cropped:
			self.currImgObj = (self.cropList[self.cropIndex])
		else:
			# null obj
			self.currImgObj = img_obj(self, nullImg)

		return self.currImgObj

def main():
	app = img()

if __name__ == "__main__":
    main()
