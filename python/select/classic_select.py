from math import ceil

INSERTATION_SORT_THRESHOLD = 7


def rselect(array, k, cmp):
	left, right = 0, len(array) - 1
	while True:
		pivot = _partition(array, left, right, cmp)
		if k > pivot:
			left = pivot + 1
		elif k < pivot:
			right = pivot - 1
		else:
			return array[pivot]


def _partition(array, low, high, cmp):
	pivot = array[low]
	i = high
	for j in range(high, low, -1):
		if cmp(array[j], pivot) > -1:
			array[i], array[j] = array[j], array[i]
			i -= 1

	array[i], array[low] = array[low], array[i]
	return i


def _insertion_sort(array, left, right, cmp):
	for i in range(left + 1, right + 1):
		j = i - 1
		key = array[i]
		while j >= left and cmp(array[j], key) > 0:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key


def dselect(array, k, cmp):
	return array[_dselect(array, 0, len(array) - 1, k, cmp)]


def _dselect(array, left, right, k, cmp):
	while True:
		sub_array_length = right - left + 1

		if sub_array_length <= INSERTATION_SORT_THRESHOLD:
			_insertion_sort(array, left, right, cmp)
			return left + k

		sub_array_count = sub_array_length // INSERTATION_SORT_THRESHOLD
		for i in range(sub_array_count):
			offset_left = i * INSERTATION_SORT_THRESHOLD
			offset_right = offset_left + INSERTATION_SORT_THRESHOLD - 1
			_insertion_sort(array, left + offset_left, left + offset_right, cmp)
			median_array_pointer = left + i
			median_position = left + offset_left + INSERTATION_SORT_THRESHOLD // 2
			array[median_array_pointer], array[median_position] = array[median_position], array[median_array_pointer]
		median_of_medians = _dselect(array, left, left + sub_array_count - 1, ceil(sub_array_count / 2), cmp)
		array[left], array[median_of_medians] = array[median_of_medians], array[left]
		pivot = _partition(array, left, right, cmp)
		candidate_statistic = pivot - left

		if k > candidate_statistic:
			left = pivot + 1
			k = k - candidate_statistic - 1
		elif k < pivot:
			right = pivot - 1
		else:
			return pivot
