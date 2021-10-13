def read_array(filename):
	f = open(filename, 'r')
	return list(map(int, f.readline().split()))
