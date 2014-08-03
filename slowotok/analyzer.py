#!/usr/bin/python

from common import SlowoTok_Coordinate
from common import SlowoTok_Answer

debug=0

class SlowoTok_Analyzer:
	def __init__(self, board):
		self.board = board # SlowoTok_Board object
		self.boardsize = board.getSize()
		self.answers = []
		self.progress = 0

	def analyze(self, dictionary):
		print "Starting analysis..."
		for line in self.board.getFields():
			for letter in line:
				if debug:
					print "Running analysis for letter: '" + letter.value + "'"
				self.analyze_recurrent(letter.coords, None, list(dictionary))
				self.progress += 6.25
				print "\t{0}% done...".format(self.progress)
		print "Finished analysis."
		self.showAnswers()

	def analyze_recurrent(self, coord, path, dictionary):
		# Check if the letter is within range of the board
		if ((coord.x < 0) or (coord.y < 0) or (coord.x >= self.boardsize) or (coord.y >= self.boardsize)):
			if debug:
				print "Coordinate out of range ({0}, {1})".format(coord.x, coord.y)
			return

		# Check if the letter is on the path already. If so, quit.
		if (path is None):
			if debug:
				print "Starting new path: ({0}, {1})".format(coord.x, coord.y)
			path = [coord]
		elif (coord in path):
			if debug:
				print "Coordinate already in path ({0}, {1})".format(coord.x, coord.y)
			return
		else:
			path.append(coord)

		new_dictionary = []
		new_word = self.board.getWordFromPath(path)

		linked_path = ''.join(["({0},{1}) ".format(coordinate.y, coordinate.x) for coordinate in path])
		if debug:
			print "Linked path: " + linked_path + ", word: '" + new_word + "'"

		for word in dictionary:
			if (word[0:len(new_word)] == new_word):
				if (new_word == word):
					if debug:
						print "Found actual answer ! Word: '{0}', Path: {1}".format(new_word.encode('utf-8'), linked_path)
					answer = SlowoTok_Answer(word, linked_path)
					if answer not in self.answers:
						self.answers.append(answer)
				else:
					new_dictionary.append(word)
					if debug:
						print "Found word that partly fits, moving to new dictionary: '" + new_word + "' to '" + word + "'"

		if debug:
			print "Reduced dictionary to '{0}' elements.".format(len(new_dictionary))

		if (len(new_dictionary) == 0):
			return

		self.analyze_recurrent(SlowoTok_Coordinate(coord.x-1, coord.y-1), list(path), list(new_dictionary))
		self.analyze_recurrent(SlowoTok_Coordinate(coord.x, coord.y-1), list(path), list(new_dictionary))
		self.analyze_recurrent(SlowoTok_Coordinate(coord.x+1, coord.y-1), list(path), list(new_dictionary))
		
		self.analyze_recurrent(SlowoTok_Coordinate(coord.x-1, coord.y), list(path), list(new_dictionary))
		self.analyze_recurrent(SlowoTok_Coordinate(coord.x+1, coord.y), list(path), list(new_dictionary))
		
		self.analyze_recurrent(SlowoTok_Coordinate(coord.x-1, coord.y+1), list(path), list(new_dictionary))
		self.analyze_recurrent(SlowoTok_Coordinate(coord.x, coord.y+1), list(path), list(new_dictionary))
		self.analyze_recurrent(SlowoTok_Coordinate(coord.x+1, coord.y+1), list(path), list(new_dictionary))

	def showAnswers(self):
		print "============== RESULT ================"
		print "Found '{0}' answers:".format(len(self.answers))
		self.answers = sorted(self.answers, key=lambda answer: len(answer.word))

		for answer in self.answers:
			answer.dump()
