from typing import IO

from model.graph import ListenableGraphNode


def read_from_adjacency_matrix(filename):
	matrix = read_matrix(filename)
	node_list = [ListenableGraphNode(i) for i in range(len(matrix))]
	r = 0
	for row in matrix:
		c = 0
		for predicate in row:
			if int(predicate) == 1:
				node_list[r].neighbours.append(node_list[c])
			c += 1
		r += 1
	return node_list


def read_matrix(filename):
	with open(filename, 'r') as f:
		raw_matrix = f.read()
		matrix_rows = raw_matrix.split('\n')
		return list(map(lambda x: list(filter(lambda p: p != '', x.split(' '))), matrix_rows))
