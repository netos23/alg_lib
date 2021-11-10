class Scanner(object):
	def __init__(self, filename):
		self.f = open(filename, 'r')

	def read_array(self):
		return list(map(int, self.f.readline().split()))

	def read_matrix(self, size):
		return [list(map(int, self.f.readline().split())) for _ in range(size)]

	def read_int(self):
		return int(self.f.readline())

	def close(self):
		self.f.close()
