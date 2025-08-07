import time

def sequential_search(arr, x):
    # Sequential search algorithm
    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False

def binary_search(arr, x):
    # Binary search algorithm
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Generate a sorted list of numbers from 1 to 10000
arr = list(range(1, 10001))

# Test the time complexity of sequential search
start = time.time()
sequential_search(arr, 10000)
end = time.time()
print("Sequential search time:", end - start, "seconds")

# Test the time complexity of binary search
start = time.time()
binary_search(arr, 10000)
end = time.time()
print("Binary search time:", end - start, "seconds")
