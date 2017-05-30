import sys
import cv2
import copy
from enum import Enum
from var import mode

# for keyboard cmds or for quiting
def key_press(event, master, imgObj):

    # if the 'r' key is pressed, reset the cropping region
    if event.keysym == 'r':
        print("points"), master.pts
        master.pts=[]
        if master.mode == mode.orig and master.imageModified == True:
            print "Clearing regions of interests..."
            imgObj.imgLive = imgObj.imgCopy.copy()

        if master.mode == mode.cropped and master.imageModified == True:
            print "Resetting Crop level..."
            imgObj.imgLive = imgObj.imgCopy.copy()

        if master.imageModified == False:
            print "Could not reset.  Nothing available to reset to."

        master.imageModified = False
        print("points after"), master.pts

    # if the 'l' key is pressed, print the pt list
    elif event.keysym == 'l':
        print "Printing points..."
        for i in range(0,len(master.pts),2):
            print master.pts[i], master.pts[i+1]

    # if the 'c' key is pressed, crop the images
    elif event.keysym == 'c':
        if len(master.pts) < 2:
            print "Could not crop.  No ROIs defined."
        else:
            print "Cropping ROIs..."
            imgObj.crop_roi()
            master.imageModified = True
            # needed to make it show image
            #cv2.waitKey(0)

    # if the 'p' key is pressed, goto processed images list
    elif event.keysym == 'p':
        imgObj.reset()

        if master.mode == mode.orig:
            master.pts = []
            if len(master.cropList) > 0:
                print "Entering cropped image list..."
                master.mode = mode.cropped
                master.update_curr_img_obj()
                master.imageModified = False
                master.setup_mode()

    # if the 'o' key is pressed, goto original :images list
    elif event.keysym == 'o':
        if master.mode == mode.cropped:
            master.pts = []
            if len(master.origList) > 0:
                print "Entering original image list..."
                master.mode = mode.orig

                master.imageModified = False
                master.setup_mode()

    #
    elif event.keysym == 'n':
        if master.mode == mode.cropped:
            if master.cropIndex > 0:
                master.cropIndex = master.cropIndex - 1

        else:
            if master.origIndex > 0:
                master.origIndex = master.origIndex - 1
            image = master.origList[master.origIndex]

        master.imageModified = False
    #
    elif event.keysym == 'm':
        if master.mode == mode.cropped:
            if master.cropIndex < len(master.cropList) - 1:
                master.cropIndex = master.cropIndex + 1

        else:
            if master.origIndex < len(master.origList) - 1:
                master.origIndex = master.origIndex + 1
            image = master.origList[master.origIndex]

        master.imageModfied = False
        #reload_image()

    # interop submission
    elif event.keysym == 'z':
        if len(master.cropList) != 0:
            print "do interop things."
        else:
            print "no targets to submit"

    # if the 'q' key is pressed, break from the loop
    elif event.keysym == 'q':
        print "Exiting on q-press"
        sys.exit(0)

# for click-n-crop feature
def mouse_press(event, master, imgObj):
    # only allow a single set of pts for cropped mode
    #if mode == imageType.cropped:
    #    pts = []
    #    image = clone.copy()
    master.pt0 = (event.x, event.y)

def mouse_release(event, master, imgObj):
    master.pt1 = (event.x, event.y)
    imgObj.make_rectangle()
