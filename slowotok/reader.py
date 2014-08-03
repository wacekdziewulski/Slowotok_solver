#!/usr/bin/python

import codecs
import sys
from common import *

class SlowoTok_Reader:
	def getBoard(self, method, param = ""):

		print "Reading board..."
		if (method == "file"):
			f = codecs.open(param, 'r', 'utf-8')
			lines = f.readlines()
		else: # (method == "text")
			lines = stdin.readlines()

		lines = [line.rstrip() for line in lines]
		output = []
		for letters in lines:
			output[len(output):] = list(letters)

		if (len(output) == 16):
			print "Board read successfully !"

		return SlowoTok_Board(output)
