import unittest
from BurchGraphClass import BurchGraph
from BurchGraphAdjList import BurchGraphAdjList
from BurchGraphAdjMatrix import BurchGraphAdjMatrix


class TestBurchGraph(unittest.TestCase):
	
	def testCreateAbsGraph(self):
		with self.assertRaises(TypeError):
			t = BurchGraph()
			del t
		
class TestBurchGraphAdjList(unittest.TestCase):
	
	def testCreateAdjListGraph(self):
		t = BurchGraphAdjList()
		print("first "+ str(t))
		self.assertIsInstance(t,BurchGraphAdjList)
		del t
		
	def testAddNode(self):
		x = BurchGraphAdjList()
		x.addNode(1)
		print("second "+str(x))
		self.assertIsInstance(x,BurchGraphAdjList)
		self.assertEqual(x.payloads,{1:None})
		self.assertEqual(x.neighbors(1),[])
		del x

class TestAddEdge(unittest.TestCase):
	
	def testAddEdge(self):
		t = BurchGraphAdjList()
		t.addNode(1)
		t.addEdge(1,2)
		print('third '+str(t))
		self.assertEqual(t.payloads,{1:None,2:None})
		del t
		
		
	




if __name__ == '__main__':
	unittest.main()