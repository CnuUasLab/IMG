class Image:

	def __init__(self):
		self.imgLive = np.zeros((1,1,3), np.uint8)
		self.imgCopy = np.zeros((1,1,3), np.uint8)

	def __init__(self, newImg):
		self.imgLive = newImg
		self.imgCopy = newImg
		self.master = master

	def new(self, newImg):
		self.imgLive = newImg
		self.imgCopy = newImg

	def reset(self):
		self.imgLive = self.imgCopy

	def getImageLive(self):
		return self.imgLive

	def cropSubImage(self, pts):
		self.imgLive 
		for i in range(0,len(pts),2):
	        # uses this formula
	        #     clone[y0:y1, x0:x1]
	        subImg = self.imgCopy[pts[i][1]:pts[i+1][1], pts[i][0]:pts[i+1][0]]

	        try:
	            # set size of new image
	            subImg = cv2.resize(subImg, (400, 400))

	            if mode != imageType.cropped:
	                croppedImages.append(roi)
	                imageModified = False
	            else:
	                # this code applies to sub-cropping for greater accurracy
	                image = roi
	                clone = image.copy()
	                croppedImages[croppedIndex] = image
	                imageModified = True
	                image_loop()
	        
	        except:
	            print "some execption was thrown and arbitrarily handled."
	            pass