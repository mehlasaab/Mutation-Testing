
import unittest
from dynamic_programming import (knapsack, longest_common_subsequence, sum_of_subset, longest_palindromic_subsequence,
    longest_increasing_subsequence,
    max_product_subarray, min_coin_change,
    optimal_bst,
    rod_cutting, word_break,
    )

class TestDynamicProgramming(unittest.TestCase):
    def test_knapsack(self):
        weights = [1, 2, 3]
        values = [10, 15, 40]
        capacity = 6
        self.assertEqual(knapsack(weights, values, capacity), 65)  # Updated expected value

    def test_longest_common_subsequence(self):
        X = "AGGTAB"
        Y = "GXTXAYB"
        self.assertEqual(longest_common_subsequence(X, Y), 4)


    def test_sum_of_subset(self):
        nums = [3, 34, 4, 12, 5, 2]
        target_sum = 9
        self.assertTrue(sum_of_subset(nums, target_sum))
    
    def test_longest_palindromic_subsequence(self):
        s = "BBABCBCAB"
        self.assertEqual(longest_palindromic_subsequence(s), 7)

    def test_longest_increasing_subsequence(self):
        nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        self.assertEqual(longest_increasing_subsequence(nums), 6)

    def test_max_product_subarray(self):
        nums = [2, 3, -2, 4, -1]
        self.assertEqual(max_product_subarray(nums), 48)

    
    def test_optimal_bst(self):
        keys = [10, 12, 20]
        freq = [34, 8, 50]
        self.assertEqual(optimal_bst(keys, freq), 142)

    def test_rod_cutting(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20]
        n = 8
        self.assertEqual(rod_cutting(prices, n), 22)

    def test_word_break(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        self.assertTrue(word_break(s, word_dict))
    
    def test_min_coin_change(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(min_coin_change(coins, amount), 3)

if __name__ == '__main__':
    unittest.main()
