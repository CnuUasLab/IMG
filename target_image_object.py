from image_object import *
import json

# inherited object from parent img_obj
class targ_img_obj(img_obj):

	def __init__(self, master, newImg):

		img_obj.__init__(self, master, newImg)
		self.imgLive = newImg.copy()
		self.imgCopy = newImg.copy()

		self.entryType1 = ""
		self.entryLat1 = ""
		self.entryLong1 = ""
		self.entryOrien1 = ""
		self.entryShape1 = ""
		self.entryBkColor1 = ""
		self.entryAlpha1 = ""
		self.entryAlphaColor1 = ""
		self.entryDesc1 = ""
		self.entryRF1 = ""

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
		self.entryType1 = self.master.entryType.get()
		self.entryLat1 = self.master.entryLat.get()
		self.entryLong1 = self.master.entryLong.get()
		self.entryOrien1 = self.master.entryOrien.get()
		self.entryShape1 = self.master.entryShape.get()
		self.entryBkColor1 = self.master.entryBkColor.get()
		self.entryAlpha1 = self.master.entryAlpha.get()
		self.entryAlphaColor1 = self.master.entryAlphaColor.get()
		self.entryDesc1 = self.master.entryDesc.get()

	def set_entry_data(self):
		self.clear_entry_data()
		self.master.entryType.insert(0, self.entryType1)
		self.master.entryLat.insert(0, self.entryLat1)
		self.master.entryLong.insert(0, self.entryLong1)
		self.master.entryOrien.insert(0, self.entryOrien1)
		self.master.entryShape.insert(0, self.entryShape1)
		self.master.entryBkColor.insert(0, self.entryBkColor1)
		self.master.entryAlpha.insert(0, self.entryAlpha1)
		self.master.entryAlphaColor.insert(0, self.entryAlphaColor1)
		self.master.entryDesc.insert(0, self.entryDesc1)

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
		help = {'type': self.entryType1, 'latitude': self.entryLat1,
		'longitude': self.entryLong1, 'orientation': self.entryOrien1, 'shape': self.entryShape1,
		'background_color': self.entryBkColor1, 'alphanumeric': self.entryAlpha1,
		'alphanumeric_color': self.entryAlphaColor1, 'description': self.entryDesc1}
		plswork_json = json.dumps(help)
		print(plswork_json)

	def get_data_for_interop(self):
		# may not be needed
		print "Placeholder, change as necessary"
		return (self.entryType1, self.entryLat1, self.entryLat1, self.entryLong1,
		self.entryOrien1, self.entryShape1, self.entryBkColor1, self.entryAlpha1,
		self.entryAlphaColor1, self.entryDesc1)
