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
			r = m + 1
		elif arr[m] < el:
			l = m + 1
		else:
			return m
	return -1


def interpolationSearch(arr, el):
	cmp = 0
	l, r = 0, len(arr) - 1
	while l < r:
		cmp += 1
		m = l + (r - l) * (el - arr[l]) // (arr[r] - arr[l])
		if arr[m] == el:
			return m
		elif arr[m] > el:
			l = m
		elif arr[m] < el:
			r = m 
	return -1

if __name__ == '__main__':
	array = IO.readArray('input.txt')
	avgL , avgB, avgI = 0, 0, 0
	for i in range(len(array)):
		cmp, index = indexOf(array, array[i])
		avgL += cmp
		
		cmp, index = binarySearch(array, array[i])
		avgB += cmp
		
		cmp, index = interpolationSearch(array, array[i])
		avgI += cmp
	print(f'linear avg cmp: {avgL / len(array)}\n')
	print(f'binary avg cmp: {avgB / len(array)}\n')
	print(f'interpolation avg cmp {avgI / len(arr)}')
