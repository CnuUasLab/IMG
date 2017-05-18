import vars
import cv2

def crop_roi():
    global image, clone, pts, croppedImages, mode, imageType, croppedIndex, imageModified

    for i in range(0,len(vars.pts),2):
        # uses this formula
        #     clone[y0:y1, x0:x1]
        roi = vars.clone[vars.pts[i][1]:vars.pts[i+1][1], vars.pts[i][0]:vars.pts[i+1][0]]

        try:
            # set size of new image
            roi = cv2.resize(roi, (400, 400))

            if vars.mode != vars.imageType.cropped:
                vars.croppedImages.append(roi)
                vars.imageModified = False
            else:
                # this code applies to sub-cropping for greater accurracy
                vars.image = roi
                vars.clone = vars.image.copy()
                vars.croppedImages[vars.croppedIndex] = vars.image
                vars.imageModified = True
        
        except:
            print "some execption was thrown and arbitrarily handled."
            pass

    vars.pts = []
        #window.attributes("-topmost", True)