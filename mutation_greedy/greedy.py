
def best_time_to_buy_and_sell_stock(prices):
    if not prices or len(prices) == 1:
        return 0

    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit

def fractional_cover_problem(values, weights, capacity):
    n = len(values)
    value_per_weight = [(v / w, v, w) for v, w in zip(values, weights)]
    value_per_weight.sort(reverse=True)

    total_value = 0
    remaining_capacity = capacity

    for vpw, v, w in value_per_weight:
        if remaining_capacity >= w:
            total_value += v
            remaining_capacity -= w
        else:
            total_value += vpw * remaining_capacity
            break

    return total_value

def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    value_per_weight = [(v / w, v, w) for v, w in zip(values, weights)]
    value_per_weight.sort(reverse=True)

    max_value = 0
    current_weight = 0

    for vpw, v, w in value_per_weight:
        if current_weight + w <= capacity:
            max_value += v
            current_weight += w
        else:
            remaining_capacity = capacity - current_weight
            max_value += vpw * remaining_capacity
            break

    return max_value

# greedy_methods.py

def gas_station(gas, cost):
    n = len(gas)

    total_gas = 0
    current_gas = 0
    start_index = 0

    for i in range(n):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            current_gas = 0
            start_index = i + 1

    return start_index if total_gas >= 0 else -1

def minimum_coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1

    return count if amount == 0 else -1

def optimal_merge_pattern(files):
    if len(files) < 2:
        return 0

    total_time = 0
    while len(files) > 1:
        files.sort()
        merge_time = files[0] + files[1]
        total_time += merge_time
        files = [merge_time] + files[2:]

    return total_time

def minimum_waiting_time(process_times):
    process_times.sort()
    total_waiting_time = 0

    for i, time in enumerate(process_times):
        total_waiting_time += time * (len(process_times) - i - 1)

    return total_waiting_time
