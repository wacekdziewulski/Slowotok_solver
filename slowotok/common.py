#!/usr/bin/python

class SlowoTok_Coordinate:
	def __init__(self, coord_x, coord_y):
		self.x = coord_x
		self.y = coord_y

	def __cmp__(self, other):
		if ((self.x == other.x) and (self.y == other.y)):
			return 0
		else:
			return 1

class SlowoTok_Letter:
	def __init__(self, value, x, y):
		self.coords = SlowoTok_Coordinate(x, y)
		self.value = value

class SlowoTok_Board:
	def __init__(self, letters):
		self.fields = [[SlowoTok_Letter(letters[(j*4)+i], j, i) for i in range(0, 4)] for j in range(0, 4)]

	def dump(self):
		print "Board looks like that:"
		for line in self.fields:
			print '\t{0} {1} {2} {3}'.format(line[0].value.encode('utf-8'), line[1].value.encode('utf-8'), line[2].value.encode('utf-8'), line[3].value.encode('utf-8'))
	
	def getFields(self):
		return self.fields

	def getSize(self):
		return len(self.fields)

	def getLetter(self, coord):
		return self.fields[coord.y][coord.x]

	def getWordFromPath(self, path):
		return ''.join([self.getLetter(coord).value for coord in path])

class SlowoTok_Answer:
	def __init__(self, word, path):
		self.word = word
		self.path = path

	def __cmp__(self, other):
		if (self.word == other.word):
			return 0
		else:
			return 1

	def dump(self):
		print "Word: '{0}', Path: {1}".format(self.word.encode('utf-8'), self.path)
