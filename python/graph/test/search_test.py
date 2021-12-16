import unittest

from gio.graph_readers import read_from_adjacency_matrix
from search.search import dfs, bfs, bfs_all


class FileTest(unittest.TestCase):

	def test_search_dfs(self):
		graph = read_from_adjacency_matrix('../assets/input.txt')
		with open(f'../assets/output_dfs.txt', 'w') as output_file:
			def before_children(node): print(f'Visit node {node.data}')

			def after_children(node): print(f'Exit node {node.data}')

			dfs(graph[0], before_children=before_children, after_children=after_children)
			visits = 0
			for node in graph:
				self.assertTrue(node.visited)
				visits += node.calls
			print(visits, file=output_file)

	def test_search_bfs(self):
		graph = read_from_adjacency_matrix('../assets/input.txt')
		with open(f'../assets/output_bfs.txt', 'w') as output_file:
			def enter_node(node, level): print(f'Visit node {node.data} on level {level}')

			bfs(graph[0], enter_node=enter_node)
			visits = 0
			for node in graph:
				self.assertTrue(node.visited)
				visits += node.calls
			print(visits, file=output_file)
