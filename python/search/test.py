from common import io_utils as IO
import search as arrays


def test(search, array, name):
	avg = 0
	for i in range(len(array)):
		index, cmp = search(array, array[i])
		avg += cmp
		if index != i:
			print('Error index missmatch')
	print(f'{name} avg cmp {avg / len(array)}\n')


if __name__ == '__main__':
	inp_arr = IO.read_array('assets/input.txt')

	test(arrays.index_of, inp_arr, 'Linaer')
	test(arrays.binary_search, inp_arr, 'Binary')
	test(arrays.interpolation_search, inp_arr, 'Interpolar')
