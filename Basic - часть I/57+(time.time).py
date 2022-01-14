# Напишите программу, чтобы получить время выполнения (в секундах) для метода Python.

import time


def sum_of_n_numbers(n):
    start_time = time.time()
    s = 1
    for i in range(1, n + 1):
        s += s ** i
    end_time = time.time()
    return end_time - start_time


print(sum_of_n_numbers(5))
