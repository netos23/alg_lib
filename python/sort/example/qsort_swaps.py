from random import randint

from common.comparators import cmp_int
from common.io_utils import scanner
from lib.classic_sorts import qsort_swaps


def gen_array(length):
	array = []
	for i in range(0, length):
		array.append(randint(0, 1000))
	return array


def get_permutations(array):
	permutations = []
	permutation = []
	chosen = [False for i in range(len(array))]

	def get_permutation():
		if len(permutation) == len(array):
			permutations.append(permutation.copy())
		else:
			for i in range(len(chosen)):
				if chosen[i]:
					continue
				chosen[i] = True
				permutation.append(array[i])
				get_permutation()
				chosen[i] = False
				permutation.pop()

	get_permutation()
	return permutations


if __name__ == '__main__':
	inp = scanner('../assets/qsort.ex')
	n = inp.read_int()
	src = gen_array(n)

	permutations = get_permutations(src)
	res = list(map(lambda a: (a, qsort_swaps(a.copy(), cmp_int)), permutations))
	res.sort(key=lambda a: a[1])

	for arr, swaps in res:
		print(f'Обменов: {swaps}\nМассив: {arr}\n')

	inp.close()
