#===========================================================#
#                                                           #
#   Description: This is the main program for the imaging   #
#              system used on the ground station.           #
#                                                           #
#                                                           #
#                   Author: daviscatherman                  #
#                  Version: 0.0.1                           #
#                                                           #
#===========================================================#

import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk
import glob
import sys
from enum import Enum
from button_press import key_press, mouse_press, mouse_release
from image_object import img_obj as img_obj
from var import mode

imgW = 1200
imgH = 800

nullImg = np.zeros((1,1,3), np.uint8)

#=======================================
#
#    Instance of the class used for the
#      main application
#
#=======================================
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

		# null obj
		self.currImgObj = img_obj(self, nullImg)

		self.import_images()

		#Set up GUI
		self.window = tk.Tk()  #Makes main window
		self.setup_GUI()


        #======================
        #
        #  Imports images to be used
        #   in the image recognition
        #   code using OpenCV
        #
        #======================
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

        #==============================
        #
        # Create the Display for the ground
        #   station team to interface with.
        #
        #==============================
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

        #==========================
        #
        # Loop method that calls
        #  show_image repeatedly.
        #
        #==========================
	def image_loop(self):
	    self.show_image()
	    self.lmain.after(100, lambda: self.lmain.focus_force())
	    self.lmain.after(250, self.image_loop)

        #===============================
        #
        # Show image in tkinter and run
        #   CV2 operations on it.
        #
        #===============================
	def show_image(self):
		self.update_curr_img_obj()
		liveImage = self.currImgObj.get_image_live()

		cv2image = cv2.cvtColor(liveImage, cv2.COLOR_BGR2RGBA)

		tempImage = Image.fromarray(cv2image)

		imgtk = ImageTk.PhotoImage(image=tempImage)
		self.lmain.imgtk = imgtk

		self.lmain.configure(image=imgtk)

        #============================
        #
        # Setup the viewing window.
        #
        #============================
	def setup_mode(self):
	    if self.mode == mode.orig:
	        self.sliderFrame.grid_forget()
	        self.window.geometry("")
	    else:
	        #Slider window (slider controls stage position)
	        self.sliderFrame = tk.Frame(self.window, width=800, height=400)
	        self.sliderFrame.grid(row = 1, column=0, padx=10, pady=2)

        #===============================
        #
        # Updates the current image with
        #  the one that is needed for operations.
        #
        #===============================
	def update_curr_img_obj(self):

		if len(self.origList) and self.mode == mode.orig:
			self.currImgObj = (self.origList[self.origIndex])
		elif len(self.cropList) and self.mode == mode.cropped:
			self.currImgObj = (self.cropList[self.cropIndex])
		else:
			# null obj
			self.currImgObj = img_obj(self, nullImg)
#===================
#
# Start main application
#
#===================
def main():
	app = img()


if __name__ == "__main__":
    main()
