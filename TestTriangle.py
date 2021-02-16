import unittest
from Triganle import classifyTraingle
class TestTriangles(unittest.TestCase):

    def test_invalid_triangles(self):
        self.assertEqual(classifyTraingle(1, 7, 88), 'Not A Triangle', '1, 7, 88 is not a Triangle')
    def test_invalid_triangles2(self):
        self.assertEqual(classifyTraingle(2, 7, 3), 'Not A Triangle', '2, 7, 3 is not a Triangle')
    def test_invalid_triangles3(self):
        self.assertEqual(classifyTraingle(4, 9, 4), 'Not A Triangle', '4, 9, 4 is not a Triangle')

    def test_right_triangles(self):
        self.assertEqual(classifyTraingle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    def test_right_triangles2(self):
        self.assertEqual(classifyTraingle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
    def test_right_triangles3(self):
        self.assertEqual(classifyTraingle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')
    
    def test_equilateral_triangles(self): 
        self.assertEqual(classifyTraingle(7,7,7), 'Equilateral', '7,7,7 should be equilateral')
    def test_equilateral_triangles2(self):
        self.assertEqual(classifyTraingle(5,5,5), 'Equilateral', '5,5,5 should be equilateral')
    def test_equilateral_triangles3(self):     
        self.assertEqual(classifyTraingle(6,6,6), 'Equilateral', '6,6,6should be equilateral')

    def test_isosceles_triangles(self):      
        self.assertEqual(classifyTraingle(6,6,4), 'Isosceles', '6,6,4 should be isosceles')
    def test_isosceles_triangles2(self):     
        self.assertEqual(classifyTraingle(7,7,5), 'Isosceles', '7,7,5 should be isosceles')
    def test_isosceles_triangles3(self):
        self.assertEqual(classifyTraingle(8,8,6), 'Isosceles', '8,8,H6 should be isosceles')

    def test_scalene_triangles(self):  
        self.assertEqual(classifyTraingle(1, 2, 3), 'Scalene', '1, 2, 3 should be scalene')
    def test_scalene_triangles2(self):    
        self.assertEqual(classifyTraingle(4, 5, 6), 'Scalene', '4, 5, 6 should be scalene')
    def test_scalene_triangles3(self):
        self.assertEqual(classifyTraingle(6, 7, 8), 'Scalene', '6, 7, 8 should be scalene')

    def test_invalid1(self):  
        self.assertEqual(classifyTraingle(300, 500, 500), 'Invalid Input', '300, 500, 19 should be invalid')
    def test_invalid2(self):
        self.assertEqual(classifyTraingle(-1, -2, -63), 'Invalid Input', '-1, -2, -63 Should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

