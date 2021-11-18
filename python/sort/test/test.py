import random
import unittest
from common.io_utils import scanner
from lib.classic_sorts import *
from common.comparators import *


class MyTestCase(unittest.TestCase):

	def test_insertion_sort_swaps(self):
		out = scanner('../assets/insertion.output')
		inp = scanner('../assets/insertion.input')

		expected_array = out.read_array()
		expected_swaps = out.read_int()

		actual_array = inp.read_array()
		actual_swaps = insertion_sort_swaps(actual_array, cmp_int)

		out.close()
		inp.close()

		self.assertEqual(expected_swaps, actual_swaps)
		self.assertEqual(expected_array, actual_array)
		print(f'Массив: {actual_array}\nОбменов: {actual_swaps}')

	def test_insertion_sort(self):
		out = scanner('../assets/insertion.output')
		inp = scanner('../assets/insertion.input')

		expected_array = out.read_array()

		actual_array = inp.read_array()
		insertion_sort(actual_array, cmp_int)

		out.close()
		inp.close()

		self.assertEqual(expected_array, actual_array)
		print(f'Массив: {actual_array}')

	def test_shell_sort(self):
		actual_array = [random.randint(0, 100) for _ in range(0, 100)]
		expected_array = actual_array.copy()
		expected_array.sort()
		shell_sort(actual_array, cmp_int)

		self.assertEqual(expected_array, actual_array)
		print(f'Массив: {actual_array}')

	def test_shell_sort_swaps(self):
		out = scanner('../assets/shell.output')
		inp = scanner('../assets/shell.input')
		f = open('../assets/shell1.wrk', 'w')

		expected_array = out.read_array()

		actual_array2 = inp.read_array()
		actual_array3 = actual_array2.copy()
		swap2 = shell_sort_swaps2(actual_array2, cmp_int)
		swap3 = shell_sort_swaps3(actual_array3, cmp_int)

		out.close()
		inp.close()

		self.assertEqual(expected_array, actual_array2)
		self.assertEqual(expected_array, actual_array3)

		print(f'Массив: {actual_array2}\n Обменов при 2x: {swap2}\n Обменов при 3х: {swap3}', file=f)
		f.close()

	def test_qsort(self):
		out = scanner('../assets/insertion.output')
		inp = scanner('../assets/insertion.input')

		expected_array = out.read_array()

		actual_array = inp.read_array()
		qsort(actual_array, cmp_int)

		out.close()
		inp.close()

		self.assertEqual(expected_array, actual_array)
		print(f'Массив: {actual_array}')


if __name__ == '__main__':
	unittest.main()
