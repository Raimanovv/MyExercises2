# Факториал через цикл

def fact(x):
    a = 1
    for i in range(2, x + 1):
        a *= i
    return a


print(fact(4))
