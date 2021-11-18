import math


def insertion_sort_swaps(array, cmp):
	return _insertion_sort_swaps(array, cmp, 1)


def insertion_sort(array, cmp):
	_insertion_sort(array, cmp, 1)


def _insertion_sort(array, cmp, inc):
	for i in range(inc, len(array), 1):
		j = i
		delta = j - inc
		while delta >= 0 and cmp(array[delta], array[j]) > 0:
			array[delta], array[j] = array[j], array[delta]
			j = delta
			delta = j - inc


def _insertion_sort_swaps(array, cmp, inc):
	swaps = 0
	for i in range(inc, len(array), 1):
		j = i
		delta = j - inc
		while delta >= 0 and cmp(array[delta], array[j]) > 0:
			swaps += 1
			array[delta], array[j] = array[j], array[delta]
			j = delta
			delta = j - inc
	return swaps


def shell_sort(array, cmp):
	_insertion_sort(array, cmp, 1)


def shell_sort_swaps2(array, cmp):
	return _shell_sort_swaps(array, cmp, lambda l: math.ceil(math.log2(l)),
							 lambda step: (pow(2, step)) - 1)


def shell_sort_swaps3(array, cmp):
	return _shell_sort_swaps(array, cmp, lambda l: math.ceil(math.log(l * 2 + 1, 3)) - 1,
							 lambda step: int(1 - (pow(3, step)) / -2) - 1)


def _shell_sort_swaps(array, cmp, init, sequence):
	swaps = 0
	step = init(len(array))
	while step >= 0:
		increment = sequence(step)
		swaps += _insertion_sort_swaps(array, cmp, increment)
		step -= 1
	return swaps


def qsort_swaps(array, cmp):
	return _qsort_swaps(array, 0, len(array) - 1, cmp)


def _qsort_swaps(array, low, high, cmp):
	swaps = 0
	if low in range(0, len(array)) and high in range(0, len(array)) and low < high:
		pivot, swaps = _partition_swaps(array, low, high, cmp)
		swaps += _qsort_swaps(array, low, pivot - 1, cmp)
		swaps += _qsort_swaps(array, pivot + 1, high, cmp)
	return swaps


def _partition_swaps(array, low, high, cmp):
	pivot = array[high]
	i = low
	swaps = 0
	for j in range(low, high):
		if cmp(array[j], pivot) < 1:
			array[i], array[j] = array[j], array[i]
			swaps += 1
			i += 1
	if i in range(0, high + 1):
		array[i], array[high] = array[high], array[i]
		swaps += 1
	return i, swaps


def qsort(array, cmp):
	return _qsort_swaps(array, 0, len(array) - 1, cmp)


def _qsort(array, low, high, cmp):
	if low in range(0, len(array)) and high in range(0, len(array)) and low < high:
		pivot = _partition(array, low, high, cmp)
		_qsort_swaps(array, low, pivot - 1, cmp)
		_qsort_swaps(array, pivot + 1, high, cmp)


def _partition(array, low, high, cmp):
	pivot = array[high]
	i = low
	for j in range(low, high):
		if cmp(array[j], pivot) < 1:
			array[i], array[j] = array[j], array[i]
			i += 1
	if i in range(0, high + 1):
		array[i], array[high] = array[high], array[i]
	return i
