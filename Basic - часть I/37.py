# Напишите программу на Python для решения (x + y) * (x + y).
# Данные испытаний : х = 4, у = 3
# Ожидаемый результат : (4 + 3) ^ 2) = 49

def equation(x, y):
    return f'({x} + {y}) ^ 2 = {(x + y) ** 2}'


print(equation(4, 3))
