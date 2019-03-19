import abc


class BurchGraph(abc.ABC):
	"""Abstract Base Class for graph. """
	
	def __init__(self):
		self.payloads = dict()

	@abc.abstractmethod
	def adjacent(self):
		pass

	@abc.abstractmethod
	def neighbors(self):
		pass

	@abc.abstractmethod
	def addEdge(self):
		pass

	@abc.abstractmethod
	def deleteEdge(self):
		pass

	@abc.abstractmethod
	def addNode(self):
		pass

	@abc.abstractmethod
	def deleteNode(self):
		pass

	@abc.abstractmethod
	def dfs(self):
		pass

	@abc.abstractmethod
	def bfs(self):
		pass
