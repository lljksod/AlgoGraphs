from BurchGraphAdjMatrix import BurchGraphAdjMatrix
import random
import time

def generateNewGraph(numberOfNodes, edgeProbability):

	generatedGraph = BurchGraphAdjMatrix()
	nodes = []
	for i in range(numberOfNodes):
		nodes.append(i)
		generatedGraph.addNode(i)


		for j in nodes:
			x = random.random()
			if x <= edgeProbability:
				generatedGraph.addEdge(j,i, weight=random.randint(1,100))

		for j in nodes:
			x = random.random()
			if x <= edgeProbability:
				generatedGraph.addEdge(i,j, weight=random.randint(1,100))

	return generatedGraph


if __name__ == '__main__':

	nodeQuantity = [2,8,64,256,1024]

	for num in nodeQuantity:
		myGraph = generateNewGraph(num, 1)

		startTime = time.time()
		dfsList = []
		myGraph.dfs(num - 1, action = (lambda x: dfsList.append(x)))
		print(str(num)+ " nodes took %s seconds." % (time.time() - startTime))
		print(dfsList)
		newGraph = myGraph.minimumSpanningTree()
		newGraph.dfs(0)
		print("Edges: ")
		print(newGraph.edges)
