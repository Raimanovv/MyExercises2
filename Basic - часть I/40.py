# Напишите программу на Python для вычисления расстояния между точками (x1, y1) и (x2, y2).
import math


def length_between_points():
    x1 = int(input('x1 = '))
    y1 = int(input('y1 = '))
    x2 = int(input('x2 = '))
    y2 = int(input('y2 = '))
    return round(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2), 3)


print(length_between_points())
