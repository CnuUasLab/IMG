import numpy as np

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
imageModified = False

class imageType:
    cropped, original, none = range(3)

mode = imageType.original