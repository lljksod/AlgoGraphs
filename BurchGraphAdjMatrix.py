from BurchGraphClass import BurchGraph

class BurchGraphAdjMatrix(BurchGraph):
	
	def __init__(self):
		self.vertices = dict()
		self.edges = []
		self.payloads = dict()

	def adjacent(self,x,y):
		if self.edges[self.vertices[x]][self.vertices[y]] == 1:
			return True
		else:
			return False

	def neighbors(self,x):
		nbors = []
		index = 0
		for edge in self.edges[self.vertices[x]]:
			if edge == 1:
				nbors.append(list(self.vertices.keys())[index])
			index += 1

		return nbors


	def addEdge(self,x,y,ypload = None):
		""" Adds edge between the provided nodes. If the second node does not exist it is
		created."""
		if x not in self.payloads.keys():
			print(str(x) + ' is not a valid node.')
			pass

		if y not in self.payloads.keys():
			self.addNode(y,ypload)

		self.edges[self.vertices[x]][self.vertices[y]] = 1



	def deleteEdge(self,x,y):
		"""Deletes edge from the adjacency list of the first node if it exists."""
		if self.edges[self.vertices[x]][self.vertices[y]] == 1:
			self.edges[self.vertices[x]][self.vertices[y]] = 0
		else:
			print("No edge to remove.")

	def addNode(self,x, payload = None):
		"""Add new node to graph, if no information is provided for the node
		contents it will be set to None"""
		if x not in self.payloads.keys():
			self.payloads[x] = payload
			self.edges.append([])
			self.vertices[x] = self.edges.index(self.edges[-1])
			while len(self.edges[self.vertices[x]]) < self.vertices[x]:
				self.edges[self.vertices[x]].append(0)

			self.edges[self.vertices[x]].append(1)
			
			for node in self.edges:
				while len(node) < self.vertices[x] + 1:
					node.append(0)
		else:
			print('Node already exists.')

	def deleteNode(self,x):
		"""Deletes node from the graph. Removes any existing edges from other nodes to the 
		node being deleted."""
		if x in self.payloads.keys():
			del self.payloads[x]

		del self.edges[self.vertices[x]]

		for node in self.edges:
			del node[self.vertices[x]]

		for node in self.vertices:
			if self.vertices[node] > self.vertices[x]:
				self.vertices[node] -= 1

		del self.vertices[x]


	def dfs(g, startNode, action = print, stack = [], visited = []):
		"""This function researched and derived from:
		https://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming
		Action can accept a lambda function to perform on each nodes payload."""
		"""
		path += [startNode]

		for neighbor in g.edges[startNode]:
			if neighbor not in path:
				path = g.dfs(neighbor, action, path)

		#action(g.payloads[startNode])
		print(startNode)

		return path
		Originally used the above method. After figuring this part out I was
		able to put together a non-recursive version of bfs below with no
		additional help. After that I went back and figured out how to make
		that work for dfs below.
		"""
		
		neighbors = list(g.edges[g.vertices[startNode]])
		stack.append(startNode)
		visited.append(startNode)
		action(startNode)
		index = 0
		for node in neighbors:
			if (node == 1) & (list(g.vertices.keys())[index] not in visited):
				g.dfs(list(g.vertices.keys())[index],stack = stack, visited = visited)
			index += 1

	def bfs(g, startNode, action = print):
		path = []
		visited = []

		path.append(startNode)


		for node in path:
			visited.append(node)
			index = 0
			for neighbor in g.edges[g.vertices[node]]:
				if (neighbor == 1) & (list(g.vertices.keys())[index] not in visited):
					path.append(list(g.vertices.keys())[index])
				index += 1
			
		print(path)
		while path:
			action(path.pop(0))




if __name__ == '__main__':
	test = BurchGraphAdjMatrix()
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
	print('nighbors of 3 =' + str(test.neighbors(0)))
	test.dfs(2)
	#test.bfs(2)