import numpy as np
import cv2
import Tkinter as tk
import Image, ImageTk
import sys

pts = []
pt0 = 0,0
pt1 = 0,0

image = np.zeros((1,1,3), np.uint8)
#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Image Manipulation Genie (IMG)")
window.config(background="#FFFFFF")

#window.geometry("%dx%d+%d+%d" % (1500, 750, 1, 1))

#Graphics window
imageFrame = tk.Frame(window, width=1500, height=750)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)

def crop_roi():
    print "cropping current ROIs"
    

# ensures positive area and draws the rectangle
def make_rectangle():

    global image, pt0, pt1

    # ensures the set of two pts is in order from lowest to highest
    # so that "high-low >= 0" is true
    pts.append(min(pt0,pt1))
    pts.append(max(pt0,pt1))

    # draws rectangle at two pts in color red (BGR) with width 2
    cv2.rectangle(image, pt0, pt1, (0, 0, 255), 2)

# for click-n-crop feature
def mouse_press(event):
    global pt0
    pt0 = event.x, event.y

def mouse_release(event):
    global pt1
    pt1 = event.x, event.y
    make_rectangle()

# for keyboard cmds or for quiting
def update_key_press(event):

    global image, clone, pts

    # if the 'r' key is pressed, reset the cropping region
    if event.keysym == 'r':
        image = clone.copy()
        pts = []
        print "Regions of interests cleared"
 
    # if the 'p' key is pressed, print the pt list
    if event.keysym == 'p':
        print "Printing points..."
        for i in range(0,len(pts),2):
            print pts[i], pts[i+1]

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
    lmain.after(10, image_loop)

def main():

    global image

    image = cv2.imread("sample.jpg")
    image = cv2.resize(image, (1500, 750))
    clone = image.copy()

    #Slider window (slider controls stage position)
    sliderFrame = tk.Frame(window, width=500, height=100)
    sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

    image_loop() # display image function

    # bind the following three to the main loop
    window.bind_all('<KeyPress>', update_key_press)
    window.bind_all('<ButtonPress-1>', mouse_press)
    window.bind_all('<ButtonRelease-1>', mouse_release)


    # run the main loop of tkinter
    window.mainloop() #Starts GUI



if __name__ == "__main__":
    main()