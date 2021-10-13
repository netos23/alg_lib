from common.io_utils import read_matrix, read_int
from matrix import det


def test(size):
	matrix = read_matrix(f'assets/input{size}.txt', size)
	exp = read_int(f'assets/output{size}.txt')
	act = det(matrix)
	if exp == act:
		print(f'Test passed. Answer: {act}')
	else:
		print(f'Test failed. Answer: {exp} Actual: {act}')


if __name__ == '__main__':
	test(3)
	test(10)
	test(13)
