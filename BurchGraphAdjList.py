from BurchGraphClass import BurchGraph

class BurchGraphAdjList(BurchGraph):
	
	def __init__(self):
		self.edges = dict()
		self.payloads = dict()

	def adjacent(self,x,y):
		if y in self.edges[x]:
			return True
		else:
			return False

	def neighbors(self,x):
		return self.edges[x]

	def addEdge(self,x,y,ypload = None):
		""" Adds edge between the provided nodes. If the second node does not exist it is
		created."""
		if x not in self.payloads.keys():
			print(str(x) + ' is not a valid node.')
			pass

		if y not in self.payloads.keys():
			self.addNode(y,ypload)

		self.edges[x].append(y)



	def deleteEdge(self,x,y):
		"""Deletes edge from the adjacency list of the first node if it exists."""
		if y in self.edges[x]:
			self.edges[x].remove(y)
		else:
			print("No edge to remove.")

	def addNode(self,x, payload = None):
		"""Add new node to graph, if no information is provided for the node
		contents it will be set to None"""
		if x not in self.payloads.keys():
			self.payloads[x] = payload
			self.edges[x] = []
		else:
			print('Node already exists.')

	def deleteNode(self,x):
		"""Deletes node from the graph. Removes any existing edges from other nodes to the 
		node being deleted."""
		if x in self.payloads.keys():
			del self.payloads[x]

		if x in self.edges.keys():
			del self.edges[x]

		for i in self.edges.keys():
			if x in self.edges[i]:
				self.edges[i].remove(x)


	def dfs(g, startNode, action = print, stack = [], visited = []):
		"""https://visualgo.net/en/dfsbfs """

		stack.append(startNode)
		visited.append(startNode)
		neighbors = g.edges[startNode]
		action(startNode)

		for node in neighbors:
			if node not in visited:
				g.dfs(node, stack = stack, visited = visited)

		
		

	def bfs(g, startNode, action = print):
		"""
		path = []
		visited = []

		path.append(startNode)

		action(startNode)

		for node in path:
			visited.append(node)
			for neighbor in g.edges[path.pop(0)]:
				if neighbor not in visited:
					path.append(neighbor)
					action(neighbor)
		"""
		stack = []
		visited = []

		stack.append(startNode)


		while stack:

			currentNode = stack.pop(0)

			if currentNode not in visited:
				visited.append(currentNode)
				action(currentNode)

				for neighbor in g.edges[currentNode]:
					if neighbor not in visited:
						stack.append(neighbor)


if __name__ == '__main__':
	test = BurchGraphAdjList()
	"""
	test.addNode('a', 2)
	test.addNode(0)
	test.addEdge('a',0)
	test.addEdge('a',1, -3)
	test.deleteEdge('a',1)
	test.deleteEdge('a',1)
	test.deleteNode(0)
	test.addEdge('a', 'b', 4)
	print(test.payloads)
	print(test.edges)
	print(test.adjacent('a','b'))
	test.addEdge('a',0, -2)
	test.addEdge('a',1, -3)
	print(test.neighbors('a'))
	lambda nodePayload: print(abs(nodePayload))
	print(test.dfs('a', action = lambda nodePayload: print(nodePayload * 2)))
	test.bfs('a')
	"""
	test.addNode(2)
	test.addEdge(2,0)
	test.addEdge(2,3)
	test.addEdge(0,2)
	test.addEdge(0,1)
	test.addEdge(1,2)
	test.addEdge(3,3)
	print(test.neighbors(2))
	test.dfs(2)
	test.bfs(2)
