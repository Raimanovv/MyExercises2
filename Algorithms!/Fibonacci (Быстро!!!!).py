t = [0] * 1000


def f(n):
    if n <= 1:
        return n
    else:
        if t[n - 1] == 0:
            t[n - 1] = f(n - 1)
        if t[n - 2] == 0:  # ????? Можно ведь без этого
            t[n - 2] = f(n - 2)  # ????? Можно ведь без этого
        t[n] = t[n - 1] + t[n - 2]
        return t[n]


print(f(10))
print(t)
