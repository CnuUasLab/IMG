import sys
import cv2
import copy
from enum import Enum
from var import mode

class imageType:
    cropped, original, none = range(3)

# for keyboard cmds or for quiting
def key_press(event, master, imgObj):

    # if the 'r' key is pressed, reset the cropping region
    if event.keysym == 'r':
        print("points"), master.pts
        if master.mode == imageType.original and master.imageModified == True:
            print "Clearing regions of interests..."
            image = copy.copy(imgObj)
            master.pts = []

        if master.mode == imageType.cropped and master.imageModified == True:
            print "Resetting Crop level..."
            image = copy.copy(tempImg)
            clone = copy.copy(tempImg)

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
        print "a p was pressed"
        print master.mode, len(master.cropList)
        if master.mode == imageType.original:
            master.pts = []
            if len(master.cropList) > 0:
                print "Entering cropped image list..."
                master.mode = imageType.cropped
                image = master.cropList[0]
                clone = copy.copy(image)
                tempImg = copy.copy(image)
                master.imageModified = False
                master.setup_mode()

    # if the 'o' key is pressed, goto original :images list
    elif event.keysym == 'o':
        if master.mode == imageType.cropped:
            master.pts = []
            if len(master.origList) > 0:
                print "Entering original image list..."
                master.mode = imageType.original
                image = master.origList[0]
                # image = cv2.resize(image, (master.imgW, master.imgH))
                clone = copy.copy(image)
                master.imageModified = False
                master.setup_mode()

    #
    elif event.keysym == 'n':
        if master.mode == imageType.cropped:
            if master.croppedIndex > 0:
                master.croppedIndex = master.croppedIndex - 1
            image = croppedImages[master.croppedIndex]
            image = cv2.resize(image, (400, 400))

        else:
            if master.origIndex > 0:
                master.origIndex = master.origIndex - 1
            image = master.origList[master.origIndex]
        clone = copy.copy(image)

        master.imageModified = False
    #
    elif event.keysym == 'm':
        if master.mode == imageType.cropped:
            if master.croppedIndex < len(croppedImages) - 1:
                master.croppedIndex = master.croppedIndex + 1
            image = croppedImages[master.croppedIndex]
            image = cv2.resize(image, (400, 400))

        else:
            if master.origIndex < len(master.origList) - 1:
                master.origIndex = master.origIndex + 1
            image = master.origList[master.origIndex]
        clone = copy.copy(image)

        master.imageModfied = False
        #reload_image()

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
