import numpy as np
import cv2
import Tkinter as tk
import Image, ImageTk
import sys

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Image Manipulation Genie (IMG)")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)

image = cv2.imread("sample.jpg")
image = cv2.resize(image, (1000, 500))
clone = image.copy()

# for keyboard cmds or for quiting
def update_key_press(event):
    global image, clone
    # if the 'r' key is pressed, reset the cropping region
    if event.keysym == 'r':
        image = clone.copy()
 
    # if the 'q' key is pressed, break from the loop
    elif event.keysym == 'q':
        sys.exit(0)

pt0 = 0,0
pt1 = 0,0

# ensures positive area and draws the rectangle
def make_rectangle():
    global image, pt0, pt1
    cv2.rectangle(image, pt0, pt1, (0, 255, 0), 2)

# for click-n-crop feature
def mouse_press(event):
    global pt0
    pt0 = event.x, event.y

def mouse_release(event):
    global pt1
    pt1 = event.x, event.y

    make_rectangle()


def show_image():

    global image, pt0, pt1

    cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)


    img = Image.fromarray(cv2image)

    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk

    lmain.configure(image=imgtk)
    lmain.after(10, show_image)

#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=500, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

show_image()  #Display 2
window.bind_all('<KeyPress>', update_key_press)
window.bind_all('<ButtonPress-1>', mouse_press)
window.bind_all('<ButtonRelease-1>', mouse_release)
window.mainloop() #Starts GUI
