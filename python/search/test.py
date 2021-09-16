import io_utils as IO
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
	array = IO.readArray('input.txt')
 
	test(arrays.indexOf, array, 'Linaer')
	test(arrays.binarySearch, array, 'Binary')
	test(arrays.interpolationSearch, array, 'Interpolar')
