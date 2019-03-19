from BurchGraphClass import BurchGraph
import heapq

if __name__ == '__main__':
	from BurchGraphAdjMatrix import BurchGraphAdjMatrix

class BurchGraphAdjList(BurchGraph):
	
	def __init__(self):
		self.edges = dict()
		self.payloads = dict()
		self.weights = dict()

	def adjacent(self,x,y):
		if y in self.edges[x]:
			return True
		else:
			return False

	def neighbors(self,x):
		return self.edges[x]

	def addEdge(self,x,y,ypload = None, weight = None):
		""" Adds edge between the provided nodes. If the second node does not exist it is
		created."""
		if x not in self.payloads.keys():
			print(str(x) + ' is not a valid node.')
			pass

		if y not in self.payloads.keys():
			self.addNode(y,ypload)

		self.edges[x].append(y)
		self.weights[x].append([y,weight])




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
			self.weights[x] = []
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

	def minimumSpanningTree(g):
		#Researched and derived from: https://gist.github.com/Peng-YM/84bd4b3f6ddcb75a147182e6bdf281a6
		#tree will be stored in a list based graph
		mst = BurchGraphAdjList()
		mst.addNode(list(g.payloads.keys())[0])
		#x will be a set used to track the vertices
		vertices = set()
		weight = 0
		#vertices.add(list(g.payloads.keys())[0])
		vert = list(g.payloads.keys())[0]

		while len(list(mst.payloads.keys())) != len(g.payloads.keys()):
			crossing = []
			#for x in vertices:
			#	"""for k in range(len(g.payloads.keys())):
			#		for sublist in g.weights[x]:
			#			if (sublist[0] == k):
			#				weight = sublist[1]
			#				break
			#			else:
			#				weight = 0"""
				#i'm leaving the above comment(docstring) in, it worked but then i came up with this and it's much more efficient
				#add all edges starting from the current vertex and their weights to a min-heap
			
			for sublist in g.weights[vert]:
				k = sublist[0]
				weight = sublist[1]
				if (weight > 0) and (k not in list(mst.payloads.keys())):
					heapq.heappush(crossing, (weight, (vert, k)))
			#get smallest weight edge from min-heap
			edge = heapq.heappop(crossing)
			#add this edge to the mst graph
			mst.addEdge(edge[1][0],edge[1][1], weight=edge[0])
			#add neighbor to vertices set to be used
			vert = edge[1][1]

			
		return mst

	def dijkstra(self, source):
		#researched and derived partially from: https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
		# https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php

		#initialize shortest path tree graph
		spt = BurchGraphAdjList()
		spt.addNode(source)
		#set var for infinity
		inf = float('inf')
		
		#set all nodes to unvisited
		unvisited = set()
		for vert in self.edges.keys():
			unvisited.add(vert)

		print(unvisited)
		#set all distances to inf then source distance to 0
		distances = {k:inf for (k,v) in self.weights.items()}
		distances[source] = 0
		while unvisited:

			#get node with smallest distance
			#https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
			currentNode = min(unvisited, key = lambda vertex: distances[vertex])
			print(currentNode)
			if distances[currentNode] == inf:
				break

			for neighbor, weight in self.weights[currentNode]:
				if neighbor in unvisited:
					newDistance = distances[currentNode] + weight

				if newDistance < distances[neighbor]:
					distances[neighbor] = newDistance
					


			unvisited.remove(currentNode)
			if len(unvisited) != 0:
				closestNeighbor = min(unvisited, key = lambda vertex: distances[vertex])
				print('closest neighbor', closestNeighbor)
				spt.addEdge(currentNode, closestNeighbor, weight=weight)

		return spt



		


def convertToList(matrixGraph):

	if type(matrixGraph) is BurchGraphAdjMatrix:
		convertedListGraph = BurchGraphAdjList()

		convertedListGraph.addNode(matrixGraph.vertices[0])

		iCoord = 0
		for vert in matrixGraph.edges:
			jCoord = 0
			for edge in vert:
				if edge == 1:
					convertedListGraph.addEdge(list(matrixGraph.vertices)[iCoord], list(matrixGraph.vertices)[jCoord])
				jCoord += 1
			iCoord += 1

		return convertedListGraph
	else:
		print("Object Must Be Matrix Graph")




if __name__ == '__main__':

	testGraph = BurchGraphAdjList()
	testGraph.addNode(0)
	testGraph.addEdge(0,1, weight=1)
	testGraph.addEdge(1,2, weight=2)
	testGraph.addEdge(2,3, weight=3)
	newGraph = testGraph.minimumSpanningTree()

	print(newGraph.edges)
	print()
	print(newGraph.weights)
	
	newGraph.dfs(0)
	testGraph.dijkstra(0)