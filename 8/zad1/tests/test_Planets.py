import unittest
import json

from sample.Planets import *



class Test(unittest.TestCase):
	def test_from_file(self):
		self.temp = Age()
		file = open("../tests/Data.json")
		testsData = json.load(file)
		file.close()
		for [input, expectedOutput] in testsData:
			self.assertEqual(self.temp.getAge(input[0], input[1]), expectedOutput)


if __name__ == "__main__":
	unittest.main()