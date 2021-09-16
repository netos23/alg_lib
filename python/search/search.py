import io_utils as IO

def indexOf(arr, el):
	cmp = 0
	for i in range(len(arr)):
		cmp += 1
		if arr[i] == el:
			return i, cmp
	return -1, cmp	


def binarySearch(arr, el):
	cmp = 0
	l, r = 0, len(arr)
	while l < r:
		cmp += 1
		m = (l+r) // 2
		if arr[m] > el:
			r = m
		elif arr[m] < el:
			l = m
		else:
			return m, cmp
	return -1, cmp


def interpolationSearch(arr, el):
	cmp = 0
	l, r = 0, len(arr) - 1
	while l < r:
		cmp += 1
		m = l + (r - l) * (el - arr[l]) // (arr[r] - arr[l])
		if arr[m] > el:
			l = m
		elif arr[m] < el:
			r = m
		else:
			return m, cmp 
	return -1, cmp

