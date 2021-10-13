# different functions for big n because rec_det too slow
def det(matrix):
	if len(matrix) <= 10:
		return rec_det(matrix)
	else:
		return gaussian_det(matrix)


def rec_det(matrix):
	size = len(matrix)
	if size == 0:
		return 0
	elif size == 1:
		return matrix[0][0]
	elif size == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	else:
		tmp, sign = 0, 1
		for c in range(0, size):
			tmp += matrix[0][c] * sign * rec_det(
				[matrix[r][0:c] + matrix[r][c + 1:size] if c < size - 1 else matrix[r][0:c] for r in range(1, size)])
			sign *= -1
		return tmp


# Its just a fast solution for n=13
# It cant be use in solutions because dont handle trailing zeroes
def gaussian_det(mat):
	matrix = mat
	size = len(matrix)
	res, sup = 1, 1
	for i in range(size):
		for r in range(i + 1, size):
			tmp = matrix[r][i]
			if matrix[i][i] != 0:
				sup *= matrix[i][i]
			for c in range(i, size):
				matrix[r][c] = matrix[i][i] * matrix[r][c] - tmp * matrix[i][c]
	for i in range(size):
		res *= matrix[i][i]
	return int(res / sup)
