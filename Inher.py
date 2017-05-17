class App:

	def __init__(self):
		self._images = []

	def addImage(self, Image):
		self._images.append(Image)

	def printImage(self):
		print self._images
		for n in range(0,len(self._images)):
			print self._images[n].getN()

class Image:

	def __init__(self, master):
		self._master = master
		self._master.addImage(self)
		self._n = 0

	def n(self, n):
		self._n = 5

	def getN(self):
		return self._n

	def printMaster(self):
		self._master.printImage()

myApp = App()
myImage = Image(myApp)
myImage.n(5)
myImage2 = Image(myApp)
myImage.printMaster()