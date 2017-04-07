import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk
import glob
import sys

import vars as v
from imageManipulation import *

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Image Manipulation Genie (IMG)")
window.config(background="#FFFFFF")


#window.geometry("%dx%d+%d+%d" % (1500, 750, 1, 1))

#Graphics window
imageFrame = tk.Frame(window, width=v.imgW, height=v.imgH)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)

def setup_mode():
    global sliderFrame
    if v.mode == v.imageType.original:
        sliderFrame.grid_forget()
        window.geometry("")
    else:       
        #Slider window (slider controls stage position)
        sliderFrame = tk.Frame(window, width=800, height=400)
        sliderFrame.grid(row = 1, column=0, padx=10, pady=2)

# ensures positive area and draws the rectangle
def make_rectangle():

    # ensures the set of two pts is in order from lowest to highest
    # so that "high-low >= 0" is true
    # always ensure the area of the pts will not be negative
    h, w, c = v.image.shape
    x0 = min(v.pt0[0],v.pt1[0], w)
    y0 = min(v.pt0[1],v.pt1[1], h)
    x1 = max(v.pt0[0],v.pt1[0], 0)
    y1 = max(v.pt0[1],v.pt1[1], 0)

    v.pts.append((x0,y0))
    v.pts.append((x1,y1))

    # draws rectangle at two pts in color red (BGR) with width 2
    cv2.rectangle(v.image, v.pt0, v.pt1, (0, 0, 255), 2)
    v.imageModified = True

# unused rn
def reload_image():
        v.image = v.croppedImages[v.croppedIndex]
        v.image = v.origImages[v.origImages]

        v.clone = v.image.copy()

# for click-n-crop feature
def mouse_press(event):

    # only allow a single set of pts for cropped mode
    if v.mode == v.imageType.cropped:
        v.pts = []
        v.image = (v.clone).copy()

    v.pt0 = event.x, event.y

def mouse_release(event):
    v.pt1 = event.x, event.y
    make_rectangle()

# for keyboard cmds or for quiting
def update_key_press(event):

    # if the 'r' key is pressed, reset the cropping region
    if event.keysym == 'r':

        if v.mode == v.imageType.original and v.imageModified == True:
            print "Clearing regions of interests..."
            image = (v.clone).copy()
            v.pts = []

        if v.mode == v.imageType.cropped and v.imageModified == True:
            print "Resetting Crop level..."
            image = (v.tempImg).copy()
            clone = (v.tempImg).copy()

        if v.imageModified == False:
            print "Could not reset.  Nothing available to reset to."
        imageModified = False

 
    # if the 'l' key is pressed, print the pt list
    elif event.keysym == 'l':
        print "Printing points..."
        for i in range(0,len(v.pts),2):
            print v.pts[i], v.pts[i+1]

    # if the 'c' key is pressed, crop the images
    elif event.keysym == 'c':
        if len(v.pts) < 2:
            print "Could not crop.  No ROIs defined."
        else:
            print "Cropping ROIs..."
            crop_roi()
            image_loop()

            # needed to make it show image
            #cv2.waitKey(0)

    # if the 'p' key is pressed, goto processed images list
    elif event.keysym == 'p':
        if v.mode == v.imageType.original:
            v.pts = []
            if len(v.croppedImages) > 0:
                print "Entering cropped image list..."
                v.mode = v.imageType.cropped
                v.image = v.croppedImages[0]
                v.clone = v.image.copy()
                v.tempImg = v.image.copy()
                v.imageModified = False
                setup_mode()

    # if the 'o' key is pressed, goto original :images list
    elif event.keysym == 'o':
        if v.mode == v.imageType.cropped:
            v.pts = []
            if len(v.origImages) > 0:
                print "Entering original image list..."
                v.mode = v.imageType.original
                v.image = v.origImages[0]
                v.image = cv2.resize(v.image, (v.imgW, v.imgH))
                v.clone = v.image.copy()
                v.imageModified = False
                setup_mode()

    #
    elif event.keysym == 'n':
        if v.mode == v.imageType.cropped:
            if v.croppedIndex > 0:
                v.croppedIndex = v.croppedIndex - 1
            v.image = v.croppedImages[v.croppedIndex]
            v.image = cv2.resize(v.image, (400, 400))

        else:
            if v.origIndex > 0:
                v.origIndex = v.origIndex - 1
            v.image = v.origImages[v.origIndex]
        v.clone = v.image.copy()

        imageModified = False
    #
    elif event.keysym == 'm':
        if v.mode == v.imageType.cropped:
            if v.croppedIndex < len(v.croppedImages) - 1:
                v.croppedIndex = v.croppedIndex + 1
            v.image = v.croppedImages[v.croppedIndex]
            v.image = cv2.resize(v.image, (400, 400))


        else:
            if v.origIndex < len(v.origImages) - 1:
                v.origIndex = v.origIndex + 1
            image = v.origImages[v.origIndex]
        v.clone = v.image.copy()

        imageModfied = False
        #reload_image()

    # if the 'q' key is pressed, break from the loop
    elif event.keysym == 'q':
        print "Exiting on q-press"
        sys.exit(0)

def show_image():

    cv2image = cv2.cvtColor(v.image, cv2.COLOR_BGR2RGBA)

    img = Image.fromarray(cv2image)

    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk

    lmain.configure(image=imgtk)

def image_loop():

    show_image()
    lmain.after(100, lambda: lmain.focus_force())
    lmain.after(250, image_loop)

def main():

    image_list = []
    for filename in glob.glob('./*.jpg'):
        im = cv2.imread(filename)
        im = cv2.resize(im, (v.imgW, v.imgH))
        #im=Image.open(filename)
        v.origImages.append(im)

    #image = cv2.imread("sample.jpg")
    v.image = v.origImages[0]
    v.clone = v.image.copy()

    image_loop() # display image function

    # bind the following three to the main loop
    window.bind_all('<KeyPress>', update_key_press)
    window.bind_all('<ButtonPress-1>', mouse_press)
    window.bind_all('<ButtonRelease-1>', mouse_release)

    # run the main loop of tkinter
    window.mainloop() #Starts GUI

if __name__ == "__main__":
    main()