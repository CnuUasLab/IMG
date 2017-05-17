# for keyboard cmds or for quiting
def update_key_press(event):

    # if the 'r' key is pressed, reset the cropping region
    if event.keysym == 'r':

        if mode == imageType.original and imageModified == True:
            print "Clearing regions of interests..."
            image = clone.copy()
            pts = []

        if mode == imageType.cropped and imageModified == True:
            print "Resetting Crop level..."
            image = tempImg.copy()
            clone = tempImg.copy()

        if imageModified == False:
            print "Could not reset.  Nothing available to reset to."
            
        imageModified = False

 
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
                imageModified = False
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
                imageModified = False
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

        imageModified = False
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

        imageModfied = False
        #reload_image()

    # if the 'q' key is pressed, break from the loop
    elif event.keysym == 'q':
        print "Exiting on q-press"
        sys.exit(0)

# for click-n-crop feature
    def mouse_press(event):
        # only allow a single set of pts for cropped mode
        if mode == imageType.cropped:
            pts = []
            image = clone.copy()

        pt0 = event.x, event.y


    def mouse_release(event):
        pt1 = event.x, event.y
        make_rectangle()