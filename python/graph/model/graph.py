class GraphNode:
	def __init__(self, data=None):
		self.data = data
		self.__visited = False
		self.neighbours = []

	def setvisited(self, value):
		self.__visited = value

	def getvisited(self):
		return self.__visited

	visited = property(fget=getvisited, fset=setvisited)


class ListenableGraphNode(GraphNode):
	def __init__(self, data=None):
		super().__init__(data)
		self.calls = 0

	def getvisited(self):
		self.calls += 1
		return super().getvisited()

	def setvisited(self, value):
		super().setvisited(value)

	visited = property(fget=getvisited, fset=setvisited)
