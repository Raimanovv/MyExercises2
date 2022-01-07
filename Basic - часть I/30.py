# Напишите программу на Python, которая примет основание и высоту треугольника и вычислит
# площадь.

def square_triangle(base, height):
    return 0.5 * base * height

base = int(input('Введите длину основания треугольника: '))
height = int(input('Введите длину высоты треугольника: '))
print(square_triangle(base, height))