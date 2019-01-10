import unittest
from BurchGraphClass import BurchGraph
from BurchGraphAdjList import BurchGraphAdjList
from BurchGraphAdjMatrix import BurchGraphAdjMatrix


class TestBurchGraph(unittest.TestCase):
	
	def testCreateAbsGraph(self):
		with self.assertRaises(TypeError):
			t = BurchGraph()
		
class TestBurchGraphAdjList(unittest.TestCase):
	
	def testCreateAdjListGraph(self):
		t = BurchGraphAdjList()
		self.assertIsInstance(t,BurchGraphAdjList)
		
	def testAddNode(self):
		x = BurchGraphAdjList()
		x.addNode(1)
		self.assertIsInstance(x,BurchGraphAdjList)
		self.assertEqual(x.payloads,{1:None})
		self.assertEqual(x.neighbors(1),[])
	
	def testAddEdge(self):
		t = BurchGraphAdjList()
		t.addNode(1)
		t.addEdge(1,2)
		self.assertEqual(t.payloads,{1:None,2:None})
		
	def testDeleteNode(self):
		t = BurchGraphAdjList()
		t.addNode(1)
		t.addEdge(1,2)
		t.deleteNode(2)
		self.assertEqual(t.payloads,{1:None})
		self.assertEqual(t.edges, {1:[]})

	def testDeleteEdge(self):
		t = BurchGraphAdjList()
		t.addNode(1)
		t.addEdge(1,2)
		t.deleteEdge(1,2)
		self.assertEqual(t.payloads,{1:None,2:None})
		self.assertEqual(t.edges,{1:[],2:[]})

	def testDeleteMoreEdges(self):
		t = BurchGraphAdjList()
		t.addNode(1)
		t.addEdge(1,2)
		t.addEdge(2,3)
		t.addEdge(3,4)
		t.addEdge(4,5)
		t.addEdge(5,6)
		t.addEdge(6,7)
		t.deleteEdge(2,3)
		t.deleteEdge(4,5)
		self.assertEqual(t.edges, {1:[2],2:[],3:[4],4:[],5:[6],6:[7],7:[]})
		t.addEdge(1,5)
		t.addEdge(1,7)
		self.assertEqual(t.edges, {1:[2,5,7],2:[],3:[4],4:[],5:[6],6:[7],7:[]})
		t.deleteEdge(1,5)
		self.assertEqual(t.edges, {1:[2,7],2:[],3:[4],4:[],5:[6],6:[7],7:[]})
	
	def testAdjacent(self):
		t = BurchGraphAdjList()
		t.addNode(1)
		t.addEdge(1,2)
		self.assertEqual(t.adjacent(1,2),True)

	def testNeighbors(self):
		t = BurchGraphAdjList()
		t.addNode(1)
		t.addEdge(1,2)
		self.assertEqual(t.neighbors(1),[2])
		t.addEdge(2,3)
		t.addEdge(2,4)
		t.addEdge(2,5)
		self.assertEqual(t.neighbors(2),[3,4,5])

	def testDfs(self):
		t = BurchGraphAdjList()
		t.addNode(1)
		t.addEdge(1,2)
		t.addEdge(1,3)
		t.addEdge(1,4)
		t.addEdge(2,4)
		t.addEdge(4,5)
		t.dfs(1)




if __name__ == '__main__':
	unittest.main()