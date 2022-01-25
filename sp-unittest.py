from spa import createSPtable, findSP, getPath, getSP
import unittest
class TestSP(unittest.TestCase):
    def setUp(self):
        self.graphInfo = [
            ['A', 'B', '5'], 
            ['A', 'D', '3'], 
            ['A', 'E', '4'], 
            ['B', 'C', '4'], 
            ['E', 'F', '6'], 
            ['C', 'G', '2'], 
            ['D', 'G', '6'], 
            ['G', 'H', '3'], 
            ['H', 'F', '5'], 
            ['I', '0', '0']]
        self.vertices = createSPtable(self.graphInfo)

    def test_num_vertices(self):
        self.assertEqual(len(self.vertices), 8)

    def test_path_to_goal(self):
        findSP(self.graphInfo, self.vertices, 'A')
        self.assertEqual(getPath(self.vertices, 'A', 'I'), 'No path')
        self.assertEqual(getSP(self.vertices, 'C'), 10)
        
if __name__ == '__main__':
    unittest.main()