import concurrent.futures
import multiprocessing

from time import sleep, perf_counter
NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]
def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f'[{multiprocessing.current_process().name}]{number}:False')
            return False
    print(f'[{multiprocessing.current_process().name}]{number}:True')
    return True

if __name__ == "__main__":
    start = perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results_thread = executor.map(is_prime, NUMBERS)
    print(f"Thread execution time: {perf_counter() - start} seconds")

    start = perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results_process = executor.map(is_prime, NUMBERS)

    print(f"Process execution time: {perf_counter() - start}")