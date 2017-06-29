from image_object import *
from datetime import datetime
import PIL.Image
import cv2
import json

# inherited object from parent img_obj
class targ_img_obj(img_obj):

	def __init__(self, master, newImg):

		img_obj.__init__(self, master, newImg)
		self.imgLive = newImg.copy()
		self.imgCopy = newImg.copy()

		self.type = ""
		self.lat = ""
		self.long = ""
		self.orien = ""
		self.shape = ""
		self.bkColor = ""
		self.alpha = ""
		self.alphaColor = ""
		self.desc = ""
		self.RF = ""

	def crop_roi(self):
		roi = self.get_roi(0)
		# this code applies to sub-cropping for greater accurracy

		self.imgLive = roi.copy()
		self.imgCopy = roi.copy()

		self.master.image_loop()

	# makes rectangle?? davis help
	def make_rectangle(self):

		# only allow 1 red rectangle
		self.reset()

		# call the super method
		img_obj.make_rectangle(self)

	# gets data from entry fields/dropdowns
	def get_entry_data(self):
		self.type = self.master.entryType.get()
		self.lat = self.master.entryLat.get()
		self.long = self.master.entryLong.get()
		self.orien = self.master.orientationValue.get()
		self.shape = self.master.shapeValue.get()
		self.bkColor = self.master.bkColorValue.get()
		self.alpha = self.master.entryAlpha.get()
		self.alphaColor = self.master.alphaColorValue.get()
		self.desc = self.master.entryDesc.get()

	# sets data in entry fields/dropdowns
	def set_entry_data(self):
		self.clear_entry_data()
		self.master.entryType.insert(0, self.type)
		self.master.entryLat.insert(0, self.lat)
		self.master.entryLong.insert(0, self.long)
		self.master.orientationValue.set(self.orien)
		self.master.shapeValue.set(self.shape)
		self.master.bkColorValue.set(self.bkColor)
		self.master.entryAlpha.insert(0, self.alpha)
		self.master.alphaColorValue.set(self.alphaColor)
		self.master.entryDesc.insert(0, self.desc)

	# clears entry fields/dropdowns
	def clear_entry_data(self):
		self.master.entryType.delete(0, 'end')
		self.master.entryLat.delete(0, 'end')
		self.master.entryLong.delete(0, 'end')
		self.master.orientationValue.set(self.master.orienVals[0])
		self.master.shapeValue.set(self.master.shapeVals[0])
		self.master.bkColorValue.set(self.master.colorVals[0])
		self.master.entryAlpha.delete(0, 'end')
		self.master.alphaColorValue.set(self.master.colorVals[0])
		self.master.entryDesc.delete(0, 'end')

	# builds json and prints it out (not finished)
	def make_json(self):
		help = {'type': self.type, 'latitude': self.lat,
		'longitude': self.long, 'orientation': self.orien, 'shape': self.shape,
		'background_color': self.bkColor, 'alphanumeric': self.alpha,
		'alphanumeric_color': self.alphaColor, 'description': self.desc}

		# not necessary, just for testing
		time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

		# TODO make this path write to the right location
		path = ''

		filename = path + 'data' + str(self.master.cropIndex) + '_' + time + '.json'

		with open(filename, 'w') as outfile:
			json.dump(help, outfile)

		imagename = "image" + str(self.master.cropIndex) + '_' + time + '.png'
		cv2.imwrite(imagename, self.imgLive)


	def get_data_for_interop(self):
		# may not be needed
		print "Placeholder, change as necessary"
		return (self.type, self.lat, self.long, self.orien, self.shape, self.bkColor, self.alpha,
		self.alphaColor, self.desc)
