import unittest
import random

from classic_select import rselect, dselect


class MyTestCase(unittest.TestCase):
	def test_rselect(self):
		array = [i for i in range(10)]
		for t in range(15):
			random.shuffle(array)
			for i in range(10):
				statistic = rselect(array, i, lambda x, y: x - y)
				self.assertEqual(statistic, i)

	def test_dselect(self):
		array = [i for i in range(100)]
		for t in range(20):
			random.shuffle(array)
			for i in range(100):
				statistic = dselect(array, i, lambda x, y: x - y)
				self.assertEqual(statistic, i)


class FileTests(unittest.TestCase):

	def test_select(self, select_function, suffix):
		input_file = open(f'../assets/input.txt', 'r')
		output_file = open(f'../assets/output_{suffix}.txt', 'w')

		k = int(input_file.readline()) - 1
		array = list(map(int, input_file.readline().split(' ')))

		answer = select_function(array, k, lambda x, y: x - y)
		print(answer, file=output_file)

		input_file.close()
		output_file.close()

	def test_rselect(self):
		self.test_select(rselect, 'r')

	def test_dselect(self):
		self.test_select(dselect, 'd')


if __name__ == '__main__':
	unittest.main()
