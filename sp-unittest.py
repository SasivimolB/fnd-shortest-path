from this import d
from spa import ShortestPath
import unittest
class TestSP(unittest.TestCase):
    spa = ShortestPath()
    def setUp(self):
        self.graphInfo = self.spa.getinfo("graph.csv")
        self.vertices = self.spa.createSPtable(self.graphInfo)
    
    def test_cost1(self):
        start = 'A'
        end = 'B'
        self.sp = self.spa.findSP(self.graphInfo, self.vertices, start, end)
        self.assertEqual(self.sp, 5)
    def test_path1(self):
        start = 'A'
        end = 'B'
        self.sp = self.spa.findSP(self.graphInfo, self.vertices, start, end)
        self.assertEqual(self.spa.getPath(self.vertices, start, end), 'A->B')

    def test_cost2(self):
        start = 'C'
        end = 'I'
        self.sp = self.spa.findSP(self.graphInfo, self.vertices, start, end)
        self.assertEqual(self.sp, 0)
    def test_path2(self):
        start = 'C'
        end = 'I'
        self.sp = self.spa.findSP(self.graphInfo, self.vertices, start, end)
        self.assertEqual(self.spa.getPath(self.vertices, start, end), 'No path')

    def test_cost3(self):
        start = 'H'
        end = 'H'
        self.sp = self.spa.findSP(self.graphInfo, self.vertices, start, end)
        self.assertEqual(self.sp, 0)
    def test_path3(self):
        start = 'H'
        end = 'H'
        self.sp = self.spa.findSP(self.graphInfo, self.vertices, start, end)
        self.assertEqual(self.spa.getPath(self.vertices, start, end), 'H->H')

    def test_cost4(self):
        start = 'P'
        end = 'A'
        self.sp = self.spa.findSP(self.graphInfo, self.vertices, start, end)
        self.assertEqual(self.sp, 0)
    def test_path4(self):
        start = 'P'
        end = 'A'
        self.sp = self.spa.findSP(self.graphInfo, self.vertices, start, end)
        self.assertEqual(self.spa.getPath(self.vertices, start, end), 'No path')

        
if __name__ == '__main__':
    unittest.main()