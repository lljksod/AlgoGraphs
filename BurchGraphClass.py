import abc

class BurchGraph(abc.ABC):
	"""Abstract Base Class for graph. Payloads is included as a dictionary so all child classes
	will have it by default. It will store the name of the node as a dictionary key, and the 
	value associated to it as the keys value. Key must be an immutable, int, string, or tupple."""
	payloads = dict()

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
