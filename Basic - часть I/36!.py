# Напишите программу на Python для добавления двух объектов, если оба объекта имеют
# целочисленный тип.

def check_int(number_1, number_2):
    if isinstance(number_1, int) and isinstance(number_2, int):
        return number_1, number_2
    raise TypeError("Inputs must be integers") # выводит ошибку

print(check_int(5, 3))
