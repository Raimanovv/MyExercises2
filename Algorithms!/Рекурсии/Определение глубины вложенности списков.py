# Определение глубины вложенности списков

a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]


def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if isinstance(i, list):
            rec(i, level + 1)


print(rec(a))
