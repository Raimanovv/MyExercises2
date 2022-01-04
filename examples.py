------------------------------------------------------
"""Всегда используем f-string python
https://shultais.education/blog/python-f-strings
Предпочитаем list comprehensions, generator expressions вместо map/filter
Используем while True для вечных циклов"""
first = 'Hello'
second = 'World'
print(f'{first}7 {8} -- {second} очень гибкий способ {round(16/5)} {second.upper()})')

--------------------------------------------------------

"""Используем list comprehensions(функция в одну строчку) 
и generator expressions (генераторное выражение)
только если есть преобразование И/ИЛИ фильтрация"""
integers = [e for e in range(10)] # если нет фильтров или преобразований, используем list
integers = list(range(10)) # Правильная версия!
print(integers)

---------------------------------------------------------

"""Пример словаря list comprehensions"""
squares = {i: i * i for i in range(10)} # Словарь
print(squares)

---------------------------------------------------------

"""# Сравнение list comprehensions с for (иногда for понятнее)"""
matrix = [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2],
]
flat = [num for row in matrix for num in row]
print(flat) # [0, 0, 0, 1, 1, 1, 2, 2, 2]

=========

matrix = [
         [0, 0, 0],
         [1, 1, 1],
         [2, 2, 2],
]
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print(flat) # [0, 0, 0, 1, 1, 1, 2, 2, 2]

----------------------------------------------------------

"""Если создать слишком большой список, то может не хватить памяти
поэтому используют генератор"""
sum([i * i for i in range(1000)]) # Список


sum(i * i for i in range(1000000000)) # Генератор (отложенные вычисления)

------------------------------------------------------------

"""generator expressions"""
my_generator = (i for i in range(10))
print(my_generator)  # < generator object < genexpr > at 0x7f17f0b14e60 >
next(my_generator)  # 0
next(my_generator)  # 1


my_sum = sum(i * i for i in range(10))  # сумма квадратов 0, 1, 4, ... 81
my_sum  # 285

--------------------------------------------------------------

"""Если список не нужен, используем generator expressions (list comprehensions без [])"""
sum(i * i for i in range(1000000000))


print(''.join(str(e) for e in range(10) if e % 2 == 0)) # sum, max, join... #02468

---------------------------------------------------------------

"""Не используем range(len(list)), если нужен индекс, то используем enumerate"""
integers = [1, 2, 3]
for index, element in enumerate(integers, 1):
    print(f'{index}--{element}')

---------------------------------------------------------------

"""Используем if collection, чтобы проверить что не пустая (список)"""
integers = [1, 2, 3]
if integers:
    print(bool(integers))

---------------------------------------------------------------

"""Используем встроенные функции python (any, all)"""
integers = [1, 2, 3]
print(all(e > 0 for e in integers)) # any, all

==============

integers = [1, 2, 3]
flag = True
for integer in integers: # неправильное решение
    if integer < 0:
        flag = False
        break
print(flag)

-----------------------------------------------------------------

"""Ловим конкретное исключение, пишем информацию в ветке except"""
integers = [1, 2, 3]
try:
    int('a')
except ValueError as e: # Это правильное оформление и решение, если надо несколько ошибок,
    print(e)            # используем несколько except
    print('Error')


integers = [1, 2, 3]
try:
    int('a')
except:   # Это неправильно (нужно ловить конкретную ошибку, иногда можно ловить все ошибки),
    pass  # а также нужно указывать тип ошибки