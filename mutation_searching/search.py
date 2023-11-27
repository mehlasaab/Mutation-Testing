

def fibonacci_search(arr, x):
    n = len(arr)
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < n:
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, n - 1)

        if arr[i] < x:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i

        elif arr[i] > x:
            fib = fib_m_minus_2
            fib_m_minus_1 -= fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1

        else:
            return i

    if offset != -1 and fib_m_minus_1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1


def binary_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

def quick_select(arr, k):
    if k > 0 and k <= len(arr):
        pivot = partition(arr, 0, len(arr) - 1)

        while pivot != k - 1:
            if pivot < k - 1:
                pivot = partition(arr, pivot + 1, len(arr) - 1)
            else:
                pivot = partition(arr, 0, pivot - 1)

        return arr[pivot]

    return None

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def ternary_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == x:
            return mid1
        elif arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            high = mid1 - 1
        elif x > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1


def jump_search(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0

    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i

    return -1

def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def tabu_search(arr, x):
    n = len(arr)
    tabu_list = [False] * n

    for i in range(n):
        if arr[i] == x:
            return i

    return -1

