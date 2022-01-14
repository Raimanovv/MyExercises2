# Напишите программу на Python для преобразования расстояния (в футах) в дюймы, ярды и мили.

def ft_convert(number):
    return f'Дюймы:{number * 12}\nЯрды:{number * 0.3333}\nМили:{number * 0.0001894}'


print(ft_convert(10))
