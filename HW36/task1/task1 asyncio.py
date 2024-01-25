import asyncio
import time

async def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

async def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

async def square(n):
    return n**2

async def cube(n):
    return n**3

async def main():
    numbers = list(range(1, 11))
    results_fibo=[]
    results_factorial=[]
    results_square=[]
    results_cube=[]
    for n in numbers:
        results = await asyncio.gather(fibonacci(n), factorial(n), square(n), cube(n))
        results_fibo.append(results[0])
        results_factorial.append(results[1])
        results_square.append(results[2])
        results_cube.append(results[3])
    print(f"{results_fibo=}")
    print(f"{results_factorial=}")
    print(f"{results_square=}")
    print(f"{results_cube=}")

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")