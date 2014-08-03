#!/usr/bin/python

from slowotok.reader import SlowoTok_Reader
from slowotok.dictionary import SlowoTok_Dictionary
from slowotok.analyzer import SlowoTok_Analyzer

dictionary = SlowoTok_Dictionary()
reader = SlowoTok_Reader()
board = reader.getBoard("file", "board")
board.dump()
analyzer = SlowoTok_Analyzer(board)
analyzer.analyze(dictionary.getDictionary())
