import numpy as np
import cv2
import sys
from enum import Enum

mode = Enum('mode', 'orig cropped')

class img_obj:

	def __init__(self, master, newImg):
		self.imgLive = newImg
		self.imgCopy = newImg
		self.master = master
		self.pts = []
		self.pt0 = 0,0

	def new(self, newImg):
		self.imgLive = newImg
		self.imgCopy = newImg

	def reset(self):
		self.imgLive = self.imgCopy

	def get_image_live(self):
		return self.imgLive

	def crop_roi(self):
		for i in range(0,len(self.pts),2):
			pts = self.pts
			# uses this formula
			#     clone[y0:y1, x0:x1]
			roi = self.imgCopy[pts[i][1]:pts[i+1][1], pts[i][0]:pts[i+1][0]]

			# set size of new image
			roi = cv2.resize(roi, (400, 400))

			if self.master.mode == mode.orig:
				tempImgObj = img_obj(self.master, roi)
				self.master.cropList.append(roi)
			else:
				# this code applies to sub-cropping for greater accurracy
				self.live = roi
				self.copy = roi

			self.master.image_loop()

	def set_pt0(self, pt0):
		self.pt0 = pt0

		# ensures positive area and draws the rectangle
	def make_rectangle(self, pt1):
		# ensures the set of two pts is in order from lowest to highest
		# so that "high-low >= 0" is true
		# always ensure the area of the pts will not be negative
		h, w, c = (self.imgLive).shape
		x0 = min(self.pt0[0],pt1[0], w)
		y0 = min(self.pt0[1],pt1[1], h)
		x1 = max(self.pt0[0],pt1[0], 0)
		y1 = max(self.pt0[1],pt1[1], 0)

		self.pts.append((x0,y0))
		self.pts.append((x1,y1))

		# draws rectangle at two pts in color red (BGR) with width 2
		cv2.rectangle(self.imgLive, self.pt0, pt1, (0, 0, 255), 2)