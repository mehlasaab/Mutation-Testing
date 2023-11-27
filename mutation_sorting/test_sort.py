import unittest
from sort import *

class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([1]), [1])
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_quick_sort(self):
        self.assertEqual(quick_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([1]), [1])
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_heap_sort(self):
        self.assertEqual(heap_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(heap_sort([]), [])
        self.assertEqual(heap_sort([1]), [1])
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_counting_sort(self):
        self.assertEqual(counting_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(counting_sort([]), [])
        self.assertEqual(counting_sort([1]), [1])
        self.assertEqual(counting_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_radix_sort(self):
        self.assertEqual(radix_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(radix_sort([]), [])
        self.assertEqual(radix_sort([1]), [1])
        self.assertEqual(radix_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_shell_sort(self):
        self.assertEqual(shell_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(shell_sort([]), [])
        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_cocktail_shaker_sort(self):
        self.assertEqual(cocktail_shaker_sort([4, 2, 7, 1, 9, 3]), [1, 2, 3, 4, 7, 9])
        self.assertEqual(cocktail_shaker_sort([]), [])
        self.assertEqual(cocktail_shaker_sort([1]), [1])
        self.assertEqual(cocktail_shaker_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
