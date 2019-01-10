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
		
		
	




if __name__ == '__main__':
	unittest.main()