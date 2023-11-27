# test_greedy_methods.py
import unittest
from greedy import best_time_to_buy_and_sell_stock, fractional_cover_problem, fractional_knapsack,gas_station, minimum_coin_change, optimal_merge_pattern, minimum_waiting_time

class TestGreedyMethods(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        self.assertEqual(best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(best_time_to_buy_and_sell_stock([1, 2, 3, 4, 5]), 4)
        self.assertEqual(best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]), 0)

    def test_fractional_cover_problem(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        self.assertEqual(fractional_cover_problem(values, weights, capacity), 240)

    def test_fractional_knapsack(self):
        weights = [10, 40, 20, 30]
        values = [60, 40, 100, 120]
        capacity = 50
        self.assertEqual(fractional_knapsack(weights, values, capacity), 240)

    def test_gas_station(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        self.assertEqual(gas_station(gas, cost), 3)

    def test_minimum_coin_change(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(minimum_coin_change(coins, amount), 3)

    def test_optimal_merge_pattern(self):
        files = [8, 4, 6, 12]
        self.assertEqual(optimal_merge_pattern(files), 58)

    def test_minimum_waiting_time(self):
        process_times = [2, 5, 1, 3]
        self.assertEqual(minimum_waiting_time(process_times), 10)



if __name__ == '__main__':
    unittest.main()
