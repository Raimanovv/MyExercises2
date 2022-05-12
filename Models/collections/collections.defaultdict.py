from collections import defaultdict

r = defaultdict(int)  # Создает словарь, который присваивает новому значению int(), то есть 0
r['s']
print(r)

b = defaultdict(list)  # Создает словарь, который присваивает новому значению list(), то есть []
b[1]
b['a'] = 123
print(b)

b.default_factory = int  # Переписывает то что присваивается
b['t']
print(b)

b.default_factory = lambda: '345'  # Переписывает то что присваивается
b['g']
print(b)

data = [
    ('ivanov', 2),
    ('petrov', 1),
    ('sidorov', 5),
    ('petrov', 3),
    ('ivanov', 2),
    ('ivanov', 4)
]
marks = defaultdict(int)
marks_list = defaultdict(list)
marks_uniq = defaultdict(set)

for surname, mark in data:
    print(surname, mark)
    marks[surname] += mark  # Подсчет значений
    marks_list[surname].append(mark)  # Группировка в список
    marks_uniq[surname].add(mark)  # Группировка уникальных значений

print(marks)
print(marks_list)
print(marks_uniq)
