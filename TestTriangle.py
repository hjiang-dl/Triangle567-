import unittest
from Triganle import classifyTriangle
class TestTriangles(unittest.TestCase):

    def test_invalid_triangles(self):
        self.assertEqual(classifyTriangle(1, 7, 88), 'NotATriangle', '1, 7, 88 is NotATriangle')
    def test_invalid_triangles2(self):
        self.assertEqual(classifyTriangle(2, 7, 3), 'NotATriangle', '2, 7, 3 is NotATriangle')
    def test_invalid_triangles3(self):
        self.assertEqual(classifyTriangle(4, 9, 4), 'NotATriangle', '4, 9, 4 is NotATriangle')

    def test_right_triangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    def test_right_triangles2(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
    def test_right_triangles3(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')
    
    def test_equilateral_triangles(self): 
        self.assertEqual(classifyTriangle(7,7,7), 'Equilateral', '7,7,7 should be equilateral')
    def test_equilateral_triangles2(self):
        self.assertEqual(classifyTriangle(5,5,5), 'Equilateral', '5,5,5 should be equilateral')
    def test_equilateral_triangles3(self):     
        self.assertEqual(classifyTriangle(6,6,6), 'Equilateral', '6,6,6should be equilateral')

    def test_Isoceles_triangles(self):      
        self.assertEqual(classifyTriangle(6,6,4), 'Isoceles', '6,6,4 should be Isoceles')
    def test_Isoceles_triangles2(self):     
        self.assertEqual(classifyTriangle(7,7,5), 'Isoceles', '7,7,5 should be Isoceles')
    def test_Isoceles_triangles3(self):
        self.assertEqual(classifyTriangle(8,8,6), 'Isoceles', '8,8,H6 should be Isoceles')

    def test_Scalene_triangles(self):  
        self.assertEqual(classifyTriangle(4, 2, 3), 'Scalene', '4, 2, 3 should be Scalene')
    def test_Scalene_triangles2(self):    
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4, 5, 6 should be Scalene')
    def test_Scalene_triangles3(self):
        self.assertEqual(classifyTriangle(6, 7, 8), 'Scalene', '6, 7, 8 should be Scalene')

    def test_invalid1(self):  
        self.assertEqual(classifyTriangle(300, 500, 500), 'InvalidInput', '300, 500, 19 should be invalid')
    def test_invalid2(self):
        self.assertEqual(classifyTriangle(-1, -2, -63), 'InvalidInput', '-1, -2, -63 Should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
