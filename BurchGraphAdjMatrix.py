from BurchGraphClass import BurchGraph
import heapq

if __name__ == '__main__':
	from BurchGraphAdjList import BurchGraphAdjList

class BurchGraphAdjMatrix(BurchGraph):
	
	def __init__(self):
		self.vertices = dict()
		self.edges = []
		self.payloads = dict()

	def adjacent(self,x,y):
		if self.edges[self.vertices[x]][self.vertices[y]] != 0:
			return True
		else:
			return False

	def neighbors(self,x):
		nbors = []
		index = 0
		for edge in self.edges[self.vertices[x]]:
			if edge != 0:
				nbors.append(list(self.vertices.keys())[index])
			index += 1

		return nbors


	def addEdge(self,x,y,ypload = None, weight = 1):
		""" Adds edge between the provided nodes. If the second node does not exist it is
		created."""
		if x not in self.payloads.keys():
			print(str(x) + ' is not a valid node.')
			pass

		if y not in self.payloads.keys():
			self.addNode(y,ypload)

		if ypload != None:
			self.edges[self.vertices[x]][self.vertices[y]] = ypload
		else:
			self.edges[self.vertices[x]][self.vertices[y]] = weight


	def deleteEdge(self,x,y):
		"""Deletes edge from the adjacency list of the first node if it exists."""
		if self.edges[self.vertices[x]][self.vertices[y]] >= 1:
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

			self.edges[self.vertices[x]].append(0)
			
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
		"""https://visualgo.net/en/dfsbfs """
		
		neighbors = list(g.edges[g.vertices[startNode]])
		stack.append(startNode)
		visited.append(startNode)
		action(startNode)
		index = 0
		for node in neighbors:
			if (node == 1) & (list(g.vertices.keys())[index] not in visited):
				g.dfs(list(g.vertices.keys())[index],action = action,stack = stack, visited = visited)
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
			
		print("path " + str(path))
		while path:
			action(path.pop(0))

	def minimumSpanningTree(g):
		#Researched and derived from: https://gist.github.com/Peng-YM/84bd4b3f6ddcb75a147182e6bdf281a6
		#tree will be stored in a list based graph
		mst = BurchGraphAdjMatrix()
		mst.addNode(list(g.vertices.keys())[0])
		#initialize weight
		weight = 0
		#set vert to first vert in new graph
		vert = list(g.vertices.keys())[0]

		#use the number of vertices added to the mst graph as the vert counter
		while len(list(mst.payloads.keys())) != len(g.payloads.keys()):
			crossing = []
			
			for k in list(g.vertices.keys()):
				weight = g.edges[vert][k]
				if (weight > 0) and (k not in list(mst.payloads.keys())):
					heapq.heappush(crossing, (weight, (vert, k)))
			#get smallest weight edge from min-heap
			edge = heapq.heappop(crossing)
			#add this edge to the mst graph
			mst.addEdge(edge[1][0],edge[1][1], weight=edge[0])
			#set neighbor as next node to be processed
			vert = edge[1][1]

			
		return mst

def convertToMatrix(listGraph):

	if type(listGraph) is BurchGraphAdjList:
		convertedMatrixGraph = BurchGraphAdjMatrix()

		convertedMatrixGraph.addNode(list(listGraph.edges.keys())[0])

		for vert in listGraph.edges:
			for edge in listGraph.edges[vert]:
				convertedMatrixGraph.addEdge(vert, edge)

		return convertedMatrixGraph
	else:
		print("Object Must Be List Graph")


if __name__ == '__main__':

	testGraph = BurchGraphAdjList()
	testGraph.addNode(0)
	testGraph.addEdge(0,1)
	testGraph.addEdge(1,2)
	testGraph.addEdge(2,3)

	newGraph = convertToMatrix(testGraph)

	if type(newGraph) is BurchGraphAdjMatrix:
		print("ok!")

	testGraph.dfs(0)
	newGraph.dfs(0)
