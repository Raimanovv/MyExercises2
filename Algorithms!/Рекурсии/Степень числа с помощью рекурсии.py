# Степень числа с помощью рекурсии, где степень может быть и положительной и отрицательной

def rec(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / rec(x, -n)
    if n % 2 == 0:
        return rec(x, n // 2) * rec(x, n // 2)
    else:
        return rec(x, n - 1) * x


print(rec(2, -1))
