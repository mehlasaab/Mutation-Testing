# array_problems.py

def max_subarray_sum(nums):
    """
    Find the contiguous subarray with the largest sum.
    """
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

def product_except_self(nums):
    """
    Given an array nums, return an array output such that output[i] is equal to
    the product of all the elements of nums except nums[i].
    """
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    left_product = right_product = 1
    for i in range(n):
        left_products[i] = left_product
        left_product *= nums[i]

        right_products[n - 1 - i] = right_product
        right_product *= nums[n - 1 - i]

    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result

def find_duplicates(nums):
    """
    Find all the duplicates in an array.
    """
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] = -nums[index]
    return duplicates

def min_subarray_len(s, nums):
    """
    Given an array of positive integers nums and a positive integer s, find the
    minimal length of a contiguous subarray whose sum is greater than or equal to s.
    """
    n = len(nums)
    start = 0
    min_len = float('inf')
    current_sum = 0

    for end in range(n):
        current_sum += nums[end]

        while current_sum >= s:
            min_len = min(min_len, end - start + 1)
            current_sum -= nums[start]
            start += 1

    return min_len if min_len != float('inf') else 0

def rotate_array(nums, k):
    """
    Rotate an array to the right by k steps.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

def move_zeros(nums):
    """
    Move all zeros to the end of an array while maintaining the relative order
    of the non-zero elements.
    """
    non_zeros = [num for num in nums if num != 0]
    zeros_count = len(nums) - len(non_zeros)
    nums[:] = non_zeros + [0] * zeros_count

def max_profit(prices):
    """
    Say you have an array prices for which the ith element is the price of a
    given stock on day i. Design an algorithm to find the maximum profit. You
    may complete as many transactions as you like (i.e., buy one and sell one
    share of the stock multiple times).
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

def remove_duplicates(nums):
    """
    Given a sorted array nums, remove the duplicates in-place such that each
    element appears only once and returns the new length.
    """
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

def trap(height):
    """
    Given n non-negative integers representing an elevation map where the width
    of each bar is 1, compute how much water it can trap after raining.
    """
    n = len(height)
    if n <= 2:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]

    return trapped_water

def max_sliding_window(nums, k):
    """
    Given an array nums, there is a sliding window of size k which is moving
    from the very left of the array to the very right. You can only see the
    k numbers in the window. Each time the sliding window moves right by one
    position.
    """
    from collections import deque

    n = len(nums)
    if n == 0:
        return []

    max_values = []
    window = deque()

    for i in range(n):
        while window and window[0] < i - k + 1:
            window.popleft()

        while window and nums[i] > nums[window[-1]]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            max_values.append(nums[window[0]])

    return max_values
