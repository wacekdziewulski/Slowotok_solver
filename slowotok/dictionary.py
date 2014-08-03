#!/usr/bin/python

import codecs

class SlowoTok_Dictionary:

	def __init__(self):
		print "Initializing dictionary..."

		f = codecs.open('dictionary', 'r', 'utf-8')
		lines = f.readlines()
		lines = [line.rstrip() for line in lines]

		self.Dictionary = lines
		
		print "Read {0} dictionary entries...".format(len(self.Dictionary))

	def getDictionary(self):
		return self.Dictionary
