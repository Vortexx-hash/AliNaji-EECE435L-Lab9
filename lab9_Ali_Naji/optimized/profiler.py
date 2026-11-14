"""Lab 9 after replacing the fast loop with an exact sum of squares."""

import time


def slow_function():
    time.sleep(2)
    total = 0
    for i in range(10000):
        total += i ** 2
    return total


def optimized_fast_function():
    # Sum of 0**2 through (n - 1)**2; exact integer arithmetic, no loop.
    n = 100
    return n * (n - 1) * (2 * n - 1) // 6


def memory_intensive_function():
    total = 0
    for i in range(10000000):
        total += i ** 2
    return total


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
