import numpy as np
import cv2
import Tkinter as tk
from Tkinter import Label, Entry
from PIL import Image, ImageTk
import glob
import sys
from enum import Enum
from button_press import key_press, mouse_press, mouse_release
from image_object import img_obj as img_obj
from var import mode
import copy

imgW = 1200
imgH = 800

nullImg = np.zeros((1,1,3), np.uint8)

class img:

	def __init__(self):
		print self
		self.cropList = []
		self.origList = []
		self.origIndex = -1
		self.cropIndex = -1
		self.imageModified = False
		# self.mode = imageType.original
		self.mode = mode.orig
		self.index = -1
		self.numOrig = 0
		self.pt0 = 0,0
		self.pt1 = 0,0
		self.pts = []
		self.imgW = 1200
		self.imgH = 800
		self.origData = [["string", "string2", "string3"], []]
		self.cropData = [[], ["string", "string2", "string3"]]

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

	def setup_GUI(self):
		self.window.wm_title("Image Manipulation Genie (IMG)")
		self.window.config(background="#FFFFFF")

		#Graphics window
		self.imageFrame = tk.Frame(self.window, width=imgW, height=imgH)
		self.imageFrame.grid(row=0, column=0, padx=10, pady=2)

		self.lmain = tk.Label(self.imageFrame)
		self.lmain.grid(row=0, column=0)

		Label(self.window, text="Color").grid(row=1, column=1)
		Label(self.window, text="Shape").grid(row=2, column=1)
		Label(self.window, text="Orientation").grid(row=3, column=1)

		self.e1 = Entry(self.window)
		self.e2 = Entry(self.window)
		self.e3 = Entry(self.window)

		self.e1.grid(row=1, column=2)
		self.e2.grid(row=2, column=2)
		self.e3.grid(row=3, column=2)

		self.image_loop() # display image function

		# bind the following three to the main loop
		self.window.bind_all('<KeyPress>', lambda event: key_press(event, self, self.currImgObj))
		self.window.bind_all('<ButtonPress-1>', lambda event: mouse_press(event, self, self.currImgObj))
		self.window.bind_all('<ButtonRelease-1>', lambda event: mouse_release(event, self, self.currImgObj))

		# run the main loop of tkinter
		self.window.mainloop() #Starts GUI

	def get_entry_data(self):
		print("one sec")

	def set_entry_data(self):
		if self.mode == mode.orig:
			print("orig")
			if(not(self.origData == [] or self.origData[self.origIndex] == [])):
				temp = copy.copy(self.origData[self.origIndex])
				self.clear_text_fields()
				if(temp[0] != ""):
					self.e1.insert(0, temp[0])
				if(temp[1] != ""):
					self.e2.insert(0, temp[1])
				if(temp[2] != ""):
					self.e3.insert(0, temp[2])
				print("not empty")
			else:
				print("empty")
				self.clear_text_fields()
		else:
			print("crop")
			if(not(self.cropData == [] or self.cropData[self.cropIndex] == [])):
				temp = copy.copy(self.cropData[self.cropIndex])
				self.clear_text_fields()
				if(temp[0] != ""):
					self.e1.insert(0, temp[0])
				if(temp[1] != ""):
					self.e2.insert(0, temp[1])
				if(temp[2] != ""):
					self.e3.insert(0, temp[2])
				print("not empty")
			else:
				print("empty")
				self.clear_text_fields()

	def clear_text_fields(self):
		self.e1.delete(0, 'end')
		self.e2.delete(0, 'end')
		self.e3.delete(0, 'end')

	def image_loop(self):
	    self.show_image()
	    self.lmain.after(100, lambda: self.lmain.focus_force())
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

	def update_curr_img_obj(self):
		if len(self.origList) and self.mode == mode.orig:
			self.currImgObj = (self.origList[self.origIndex])
		elif len(self.cropList) and self.mode == mode.cropped:
			self.currImgObj = (self.cropList[self.cropIndex])
		else:
			# null obj
			self.currImgObj = img_obj(self, nullImg)

def main():
	app = img()

if __name__ == "__main__":
    main()
