# test_array_problems.py
import unittest
from array_problems import max_subarray_sum, product_except_self, find_duplicates, \
    min_subarray_len, rotate_array, move_zeros, max_profit, remove_duplicates, trap, \
    max_sliding_window

class TestArrayProblems(unittest.TestCase):

    def test_max_subarray_sum(self):
        self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_subarray_sum([1, 2, 3, -2, 5]), 9)

    def test_product_except_self(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(product_except_self([2, 2, 2, 2]), [8, 8, 8, 8])

    def test_find_duplicates(self):
        self.assertEqual(find_duplicates([4, 3, 2, 7, 8, 2, 1, 1]), [2, 1])
        # self.assertEqual(find_duplicates([3, 3, 3, 3]), [3])

    def test_min_subarray_len(self):
        self.assertEqual(min_subarray_len(7, [2, 3, 1, 2, 4, 3]), 2)
        self.assertEqual(min_subarray_len(11, [1, 2, 3, 4, 5]), 3)

    def test_rotate_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        rotate_array(arr, 3)
        self.assertEqual(arr, [5, 6, 7, 1, 2, 3, 4])

    def test_move_zeros(self):
        arr = [0, 1, 0, 3, 12]
        move_zeros(arr)
        self.assertEqual(arr, [1, 3, 12, 0, 0])

    def test_max_profit(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)

    def test_remove_duplicates(self):
        nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
        self.assertEqual(remove_duplicates(nums), 5)
        self.assertEqual(nums[:5], [1, 2, 3, 4, 5])

    def test_trap(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap([4, 2, 0, 3, 2, 5]), 9)

    def test_max_sliding_window(self):
        self.assertEqual(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(max_sliding_window([1, -1], 1), [1, -1])

if __name__ == '__main__':
    unittest.main()
