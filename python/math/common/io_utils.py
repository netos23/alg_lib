def read_array(filename):
	f = open(filename, 'r')
	return list(map(int, f.readline().split()))


def read_matrix(filename, size):
	f = open(filename, 'r')
	return [list(map(int, f.readline().split())) for _ in range(size)]


def read_int(filename):
	return int(open(filename, 'r').readline())
