import unittest
import compute_stats2

# Create the class for all of the tests...
class Numbers_test(unittest.TestCase):

    #Test even numbered list. 
    def test_even(self):
        lst = [3, 4, 6, 8]
        self.assertEqual(compute_stats2.compute_stats(lst),(3,8,5.25,5))

    #Test odd numbered list.
    def test_odd(self):
        lst = [5, 7, 9]
        self.assertEqual(compute_stats2.compute_stats(lst),(5, 9, 7, 7))

    #Test empty list. 
    def test_empty(self):
        lst = []
        self.assertEqual(compute_stats2.compute_stats(lst),(None, None, None, None))

    #Test single element list. 
    def test_single(self):
        lst = [1]
        self.assertEqual(compute_stats2.compute_stats(lst),(1, 1, 1, 1))


if __name__ == "__main__":
    unittest.main()
