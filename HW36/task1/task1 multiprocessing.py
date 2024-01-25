import concurrent.futures
import time
from time import perf_counter


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def square(n):
    return n**2

def cube(n):
    return n**3

def main():
    n = list(range(1, 11))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results_fibo = list(executor.map(fibonacci, n))
        results_square = list(executor.map(square, n))
        results_cube = list(executor.map(cube, n))
        results_factorial = list(executor.map(factorial, n))
    print(f"{results_fibo=}")
    print(f"{results_factorial=}")
    print(f"{results_square=}")
    print(f"{results_cube=}")
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")