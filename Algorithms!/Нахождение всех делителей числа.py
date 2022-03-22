# https://stepik.org/lesson/296955/step/1?unit=278683
# Нахождение всех делителей числа
# Лучшее решение

n = int(input('Введите число: '))
i = 1
a = []


while i * i <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)
