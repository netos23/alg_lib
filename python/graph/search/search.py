from model.graph import GraphNode


def dfs_all(graph, before_child=None, after_child=None, before_children=None, after_children=None):
	for node in graph:
		if node.visited:
			continue
		dfs(node, before_child, after_child, before_children, after_children)


def dfs(target: GraphNode, before_child=None, after_child=None, before_children=None, after_children=None):
	if target.visited:
		return
	target.visited = True
	safe_call(before_children)(target)
	for neighbour in target.neighbours:
		safe_call(before_child)(target)
		dfs(neighbour, before_child, after_child, before_children, after_children)
		safe_call(after_child)(target)
	safe_call(after_children)(target)


def bfs_all(graph, enter_node=None):
	for node in graph:
		if node.visited:
			continue
		bfs(node, enter_node)


def bfs(root: GraphNode, enter_node=None):
	root.visited = True
	queue = [(root, 0)]
	while len(queue) != 0:
		target, level = queue.pop(0)
		safe_call(enter_node)(target, level)
		for neighbour in target.neighbours:
			if neighbour.visited:
				continue
			neighbour.visited = True
			queue.append((neighbour, level + 1))


def safe_call(function):
	def wrapper(*args):
		if function is not None:
			function(*args)

	return wrapper
