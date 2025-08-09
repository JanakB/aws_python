import time

# Euclidean Algorithm
def gcd_euclidean(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclidean(b, a % b)

# General GCD Algorithm
def gcd_general(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    elif a < b:
        return gcd_general(a, b % a)
    else:
        return gcd_general(a % b, b)

# Test the algorithms with increasing input sizes
for n in range(1000, 11000, 1000):
    a = n
    b = n // 2

    # Time the Euclidean Algorithm
    start_time = time.time()
    gcd_euclidean(a, b)
    end_time = time.time()
    euclidean_time = end_time - start_time

    # Time the General GCD Algorithm
    start_time = time.time()
    gcd_general(a, b)
    end_time = time.time()
    general_time = end_time - start_time

    # Print the results
    print(f"Input size: {n}")
    print(f"Euclidean Algorithm: {euclidean_time:.6f} seconds")
    print(f"General GCD Algorithm: {general_time:.6f} seconds")
    print()