# Напишите программу на Python, чтобы получить наименьшее общее кратное (LCM)
# из двух натуральных чисел.

def lcm(number_1, number_2):
    if number_1 > number_2:
        z = number_1
    else:
        z = number_2
    while True:
        if z % number_2 == 0 and z % number_1 == 0:
            lcm = z # Не очень понял, надо разобраться
            break
        z += 1
    return lcm


print(lcm(4, 6))
print(lcm(15, 17))
print(lcm(15, 31))
print(lcm(155, 144))