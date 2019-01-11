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
				generatedGraph.addEdge(i,j)

	return generatedGraph


if __name__ == '__main__':

	nodeQuantity = [2,8,64,256,1024]

	for num in nodeQuantity:
		myGraph = generateNewGraph(num, .5)

		startTime = time.time()
		dfsList = []
		myGraph.dfs(num - 1, action = (lambda x: dfsList.append(x)))
		print(str(num)+ " nodes took %s seconds." % (time.time() - startTime))
		print(dfsList)
