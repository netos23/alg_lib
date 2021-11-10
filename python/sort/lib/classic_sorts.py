def insertion_sort_swaps(array, cmp):
	swaps = 0
	for i in range(1, len(array)):
		j = i - 1
		key = array[i]
		while j >= 0 and cmp(array[j], key) > 0:
			array[j + 1] = array[j]
			swaps += 1
			j -= 1
		array[j + 1] = key
	return swaps


def insertion_sort(array, cmp):
	for i in range(1, len(array)):
		j = i - 1
		key = array[i]
		while j >= 0 and cmp(array[j], key) > 0:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
