import unittest
from common.io_utils import Scanner
from lib.classic_sorts import *
from common.comparators import *


class MyTestCase(unittest.TestCase):

	def test_insertion_sort(self):
		out = Scanner('assets/insertion.output')
		inp = Scanner('assets/insertion.input')

		expected_array = out.read_array()
		expected_swaps = out.read_int()

		actual_array = inp.read_array()
		actual_swaps = insertion_sort(actual_array, cmp_int)

		out.close()
		inp.close()

		self.assertEqual(expected_swaps, actual_swaps)
		self.assertEqual(expected_array, actual_array)
		print(f'Массив: {actual_array}\nОбменов: {actual_swaps}')


if __name__ == '__main__':
	unittest.main()
