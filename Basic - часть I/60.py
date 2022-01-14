# Напишите программу на Python для вычисления гипотенузы прямоугольного треугольника

import math


def hypotenuse_L90(h, l):
    return math.sqrt(h ** 2 + l ** 2)


print(hypotenuse_L90(3, 4))
