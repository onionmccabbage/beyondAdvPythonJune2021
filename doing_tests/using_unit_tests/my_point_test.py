# testing the Point class
from my_point import Point
import unittest

class testPoint(unittest.TestCase):
    def setUp(self):
        # this will be called before each test
        self.point = Point(3, 5)

    def testMoveBy(self):
        self.point.move_by(5, 2)
        self.assertEqual(self.point.display(), (8, 7))

    def testPointCounter(self):
        self.assertGreater(Point.points, 0)

    def testMoveByAgain(self):
        self.point.move_by(-5, -2)
        self.assertEqual(self.point.display(), (-2, 3))

    def testHypot(self):
        self.point.move_by(0,-1) # now at (3, 4)
        r = self.point.hypot()
        self.assertAlmostEqual(r, 5.00, places=2) 

    def testStringValueFails(self):
        with self.assertRaises(TypeError):
            Point('3', 4)     

if __name__ == '__main__':
    unittest.main() # this will run all tests