import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk
import glob
import sys
from enum import Enum
from KeyPress import update_key_press
from image_unit import img as img

imgW = 1200
imgH = 800

mode = Enum('mode', 'orig cropped')

class img2:

	def __init__(self):
		self.cropList = []
		self.origList = []

		self.importImages()
		self.mode = mode.orig
		self.index = 0

		#Set up GUI
		self.window = tk.Tk()  #Makes main window
		self.setupGUI()

	def importImages(self):
		for filename in glob.glob('./*.jpg'):
			img = cv2.imread(filename)
	    	img = cv2.resize(img, (imgW, imgH))
	    	imgObj = image(img, self)

	        self.origList.append(imgObj)
	        print "image imported",filename

	def setupGUI(self):

		self.window.wm_title("Image Manipulation Genie (IMG)")
		self.window.config(background="#FFFFFF")

		#Graphics window
		self.imageFrame = tk.Frame(self.window, width=imgW, height=imgH)
		self.imageFrame.grid(row=0, column=0, padx=10, pady=2)

		self.lmain = tk.Label(self.imageFrame)
		self.lmain.grid(row=0, column=0)

		self.image_loop() # display image function

		# bind the following three to the main loop
		self.window.bind_all('<KeyPress>', update_key_press)
		self.window.bind_all('<ButtonPress-1>', mouse_press)
		self.window.bind_all('<ButtonRelease-1>', mouse_release)

		# run the main loop of tkinter
		self.window.mainloop() #Starts GUI

	def image_loop(self):
	    self.show_image()
	    self.lmain.after(100, lambda: self.lmain.focus_force())
	    self.lmain.after(250, self.image_loop)

	def show_image(self):
		liveImage = (self.origList[self.index]).getImageLive()

		cv2image = cv2.cvtColor(liveImage, cv2.COLOR_BGR2RGBA)

		print liveImage, cv2image
		print "test"
    	img = Image.fromarray(cv2image)

    	imgtk = ImageTk.PhotoImage(image=img)
    	lmain.imgtk = imgtk

    	lmain.configure(image=imgtk)

	def setup_mode(self):
	    if self.mode == mode.orig:
	        self.sliderFrame.grid_forget()
	        self.window.geometry("")
	    else:       
	        #Slider window (slider controls stage position)
	        self.sliderFrame = tk.Frame(window, width=800, height=400)
	        self.sliderFrame.grid(row = 1, column=0, padx=10, pady=2)
        
def main():
	app = img2()

if __name__ == "__main__":
    main()