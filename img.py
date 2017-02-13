import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk
import glob
import sys

pts = []
pt0 = 0,0
pt1 = 0,0

imgW = 1200
imgH = 800

image = np.zeros((1,1,3), np.uint8)
clone = image.copy()
tempImg = image.copy()

croppedImages = []
origImages = []
croppedIndex  = 0
origIndex = 0

class imageType:
    cropped, original, none = range(3)

mode = imageType.original

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Image Manipulation Genie (IMG)")
window.config(background="#FFFFFF")

#window.geometry("%dx%d+%d+%d" % (1500, 750, 1, 1))

#Graphics window
imageFrame = tk.Frame(window, width=imgW, height=imgH)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)

def setup_mode():
    global mode, imageType, sliderFrame

    if mode == imageType.original:
        sliderFrame.grid_forget()
        window.geometry("")
    else:       
        #Slider window (slider controls stage position)
        sliderFrame = tk.Frame(window, width=800, height=400)
        sliderFrame.grid(row = 1, column=0, padx=10, pady=2)
        

def crop_roi():
    global image, clone, pts, croppedImages, mode, imageType

    for i in range(0,len(pts),2):
        # uses this formula
        #     clone[y0:y1, x0:x1]
        roi = clone[pts[i][1]:pts[i+1][1], pts[i][0]:pts[i+1][0]]

        try:
            # set size of new image
            roi = cv2.resize(roi, (400, 400))

            if mode != imageType.cropped:
                croppedImages.append(roi)
            else:
                # this code applies to sub-cropping for greater accurracy
                image = roi
                clone = image.copy()
                croppedImages[0] = image
                image_loop()
        
        except:
            print "some execption was thrown and arbitrarily handled."
            pass
        #window.attributes("-topmost", True)
    

# ensures positive area and draws the rectangle
def make_rectangle():

    global image, pt0, pt1

    # ensures the set of two pts is in order from lowest to highest
    # so that "high-low >= 0" is true
    # always ensure the area of the pts will not be negative
    h, w, c = image.shape
    x0 = min(pt0[0],pt1[0], w)
    y0 = min(pt0[1],pt1[1], h)
    x1 = max(pt0[0],pt1[0], 0)
    y1 = max(pt0[1],pt1[1], 0)

    pts.append((x0,y0))
    pts.append((x1,y1))

    # draws rectangle at two pts in color red (BGR) with width 2
    cv2.rectangle(image, pt0, pt1, (0, 0, 255), 2)

# 
def reload_image():
        image = croppedImages[croppedIndex]
        image = origImages[origImages]

        clone = image.copy()

# for click-n-crop feature
def mouse_press(event):
    global pt0, pts, mode, imageType, image, clone

    # only allow a single set of pts for cropped mode
    if mode == imageType.cropped:
        pts = []
        image = clone.copy()

    pt0 = event.x, event.y

def mouse_release(event):
    global pt1
    pt1 = event.x, event.y
    make_rectangle()

# for keyboard cmds or for quiting
def update_key_press(event):

    global image, clone, tempImg, pts, mode, imageType, croppedIndex, origIndex

    # if the 'r' key is pressed, reset the cropping region
    if event.keysym == 'r':

        print "Clearing regions of interests..."
        image = clone.copy()
        pts = []

        if mode == imageType.cropped:
            print "Resetting Crop level..."
            image = tempImg.copy()
            clone = tempImg.copy()

 
    # if the 'l' key is pressed, print the pt list
    elif event.keysym == 'l':
        print "Printing points..."
        for i in range(0,len(pts),2):
            print pts[i], pts[i+1]

    # if the 'c' key is pressed, crop the images
    elif event.keysym == 'c':
        if len(pts) < 2:
            print "Could not crop.  No ROIs defined."
        else:
            print "Cropping ROIs..."

            crop_roi()

            # needed to make it show image
            #cv2.waitKey(0)

    # if the 'p' key is pressed, goto processed images list
    elif event.keysym == 'p':
        if mode == imageType.original:
            pts = []
            if len(croppedImages) > 0:
                print "Entering cropped image list..."
                mode = imageType.cropped
                image = croppedImages[0]
                clone = image.copy()
                tempImg = image.copy()
                setup_mode()

    # if the 'o' key is pressed, goto original :images list
    elif event.keysym == 'o':
        if mode == imageType.cropped:
            pts = []
            if len(origImages) > 0:
                print "Entering original image list..."
                mode = imageType.original
                image = origImages[0]
                image = cv2.resize(image, (imgW, imgH))
                clone = image.copy()
                setup_mode()

    #
    elif event.keysym == 'n':
        if mode == imageType.cropped:
            if croppedIndex > 0:
                croppedIndex = croppedIndex - 1
            image = croppedImages[croppedIndex]
            image = cv2.resize(image, (400, 400))

        else:
            if origIndex > 0:
                origIndex = origIndex - 1
            image = origImages[origIndex]
        clone = image.copy()

    #
    elif event.keysym == 'm':
        if mode == imageType.cropped:
            if croppedIndex < len(croppedImages) - 1:
                croppedIndex = croppedIndex + 1
            image = croppedImages[croppedIndex]
            image = cv2.resize(image, (400, 400))

        else:
            if origIndex < len(origImages) - 1:
                origIndex = origIndex + 1
            image = origImages[origIndex]
        clone = image.copy()
        #reload_image()

    # if the 'q' key is pressed, break from the loop
    elif event.keysym == 'q':
        print "Exiting on q-press"
        sys.exit(0)

def show_image():

    global image, pt0, pt1

    cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

    img = Image.fromarray(cv2image)

    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk

    lmain.configure(image=imgtk)

def image_loop():

    show_image()
    lmain.after(100, lambda: lmain.focus_force())
    lmain.after(250, image_loop)

def main():

    global image, clone

    image_list = []
    for filename in glob.glob('./*.jpg'):
        im = cv2.imread(filename)
        im = cv2.resize(im, (imgW, imgH))
        #im=Image.open(filename)
        origImages.append(im)

    #image = cv2.imread("sample.jpg")
    image = origImages[0]
    clone = image.copy()

    image_loop() # display image function

    # bind the following three to the main loop
    window.bind_all('<KeyPress>', update_key_press)
    window.bind_all('<ButtonPress-1>', mouse_press)
    window.bind_all('<ButtonRelease-1>', mouse_release)

    # run the main loop of tkinter
    window.mainloop() #Starts GUI

if __name__ == "__main__":
    main()