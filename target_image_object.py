from image_object import *

# inherited object from parent img_obj
class targ_img_obj(img_obj):

	def __init__(self, master, newImg):

		img_obj.__init__(self, master, newImg)
		self.imgLive = newImg.copy()
		self.imgCopy = newImg.copy()

		self.orientation = "0"
		self.colorBackground = "Black"
		self.colorLetter = "Black"
		self.letter = "A"
		self.shape = "Square"

	def crop_roi(self):
		
		# get the roi in a 400x400p image
		roi = self.get_roi(0)

		# update the images
		self.imgLive = roi.copy()
		self.imgCopy = roi.copy()

		self.master.image_loop()
	
	def make_rectangle(self):

		# only allow 1 red rectangle
		self.reset()

		# call the super method
		img_obj.make_rectangle(self)

	def get_data_for_interop(self):
		# may not be needed
		print "Placeholder, change as necessary"
		return (self.orientation, self.colorBackground, self.colorLetter, self.letter, self.shape)



