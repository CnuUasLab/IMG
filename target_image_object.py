from image_object import *
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

		self.orien = {'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'}
		self.shapes = {'circle', 'semicircle', 'quarter_circle', 'triangle',
		'square', 'rectangle', 'trapezoid', 'pentagon', 'hexagon', 'heptagon',
		'octagon', 'star', 'cross'}
		self.colors = {'white', 'black', 'gray', 'red', 'blue', 'green', 'yellow',
		'purple', 'brown', 'orange'}


	def crop_roi(self):

		roi = self.get_roi(0)

		# this code applies to sub-cropping for greater accurracy
		self.imgLive = roi.copy()
		self.imgCopy = roi.copy()

		self.master.image_loop()

	def make_rectangle(self):
		self.reset()
		img_obj.make_rectangle(self)

	def get_entry_data(self):
		self.type = self.master.entryType.get()
		self.lat = self.master.entryLat.get()
		self.long = self.master.entryLong.get()
		self.orien = self.master.entryOrien.get()
		self.shape = self.master.entryShape.get()
		self.bkColor = self.master.entryBkColor.get()
		self.alpha = self.master.entryAlpha.get()
		self.alphaColor = self.master.entryAlphaColor.get()
		self.desc = self.master.entryDesc.get()

	def set_entry_data(self):
		self.clear_entry_data()
		self.master.entryType.insert(0, self.type)
		self.master.entryLat.insert(0, self.lat)
		self.master.entryLong.insert(0, self.long)
		self.master.entryOrien.insert(0, self.orien)
		self.master.entryShape.insert(0, self.shape)
		self.master.entryBkColor.insert(0, self.bkColor)
		self.master.entryAlpha.insert(0, self.alpha)
		self.master.entryAlphaColor.insert(0, self.alphaColor)
		self.master.entryDesc.insert(0, self.desc)

	def clear_entry_data(self):
		self.master.entryType.delete(0, 'end')
		self.master.entryLat.delete(0, 'end')
		self.master.entryLong.delete(0, 'end')
		self.master.entryOrien.delete(0, 'end')
		self.master.entryShape.delete(0, 'end')
		self.master.entryBkColor.delete(0, 'end')
		self.master.entryAlpha.delete(0, 'end')
		self.master.entryAlphaColor.delete(0, 'end')
		self.master.entryDesc.delete(0, 'end')

	def make_json(self):
		help = {'type': self.type, 'latitude': self.lat,
		'longitude': self.long, 'orientation': self.orien, 'shape': self.shape,
		'background_color': self.bkColor, 'alphanumeric': self.alpha,
		'alphanumeric_color': self.alphaColor, 'description': self.desc}
		plswork_json = json.dumps(help)
		print(plswork_json)

	def get_data_for_interop(self):
		# may not be needed
		print "Placeholder, change as necessary"
		return (self.type, self.lat, self.long, self.orien, self.shape, self.bkColor, self.alpha,
		self.alphaColor, self.desc)
