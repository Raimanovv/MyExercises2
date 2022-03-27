def fib(n):
    x, y = 0, 1
    for _ in range(int(n)):
        x, y = y, x + y
    return x


print(fib(5))
