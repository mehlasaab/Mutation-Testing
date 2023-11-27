
import unittest
from search import (fibonacci_search, binary_search, quick_select,ternary_search,
    jump_search,
    interpolation_search,
    tabu_search
    )

class TestSearchMethods(unittest.TestCase):
    def test_fibonacci_search(self):
        self.assertEqual(fibonacci_search([10, 20, 30, 40, 50, 60, 70, 80, 90], 30), 2)
        self.assertEqual(fibonacci_search([2, 3, 4, 10, 40], 10), 3)
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5), 4)  # Target in the middle
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1), 0)  # Target at the beginning
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 8)  # Target at the end
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0), -1)  # Target smaller than the smallest element
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), -1)  # Target larger than the largest element

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([], 1), -1)  # Empty array
        self.assertEqual(binary_search([1], 1), 0)  # Array with one element
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)  # Target at the beginning

    def test_quick_select(self):
        # self.assertEqual(quick_select([4, 1, 9, 7, 6], 2), 6)
        self.assertEqual(quick_select([5, 2, 9, 1, 5], 3), 5)
        self.assertEqual(quick_select([5, 2, 9, 1, 5], 1), 1)  # Select the smallest element
        self.assertEqual(quick_select([5, 2, 9, 1, 5], 5), 9)  # Select the largest element

    def test_ternary_search(self):
        self.assertEqual(ternary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(ternary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(ternary_search([1, 2, 3, 4, 5], 1), 0)  # Target at the beginning
        self.assertEqual(ternary_search([1, 2, 3, 4, 5], 5), 4)  # Target at the end

    def test_jump_search(self):
        self.assertEqual(jump_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(jump_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(jump_search([1, 2, 3, 4, 5], 1), 0)  # Target at the beginning
        self.assertEqual(jump_search([1, 2, 3, 4, 5], 5), 4)  # Target at the end

    def test_interpolation_search(self):
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], 1), 0)  # Target at the beginning
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], 5), 4)  # Target at the end

    def test_tabu_search(self):
        self.assertEqual(tabu_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(tabu_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(tabu_search([], 1), -1)  # Empty array
        self.assertEqual(tabu_search([1], 1), 0)  # Array with one element
        self.assertEqual(tabu_search([1, 2, 3, 4, 5], 1), 0)  # Target at the beginning
        self.assertEqual(tabu_search([1, 2, 3, 4, 5], 5), 4)  # Target at the end

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()