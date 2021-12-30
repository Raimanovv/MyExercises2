# Напишите программу на Python, которая принимает целое число (n) и
# вычисляет значение n + nn + nnn.
n = int(input('number: '))
n1 = int('{0}{0}'.format(n))
n2 = int('{0}{0}{0}'.format(n))
print(n + n1 +n2)