# Счетчик

from collections import Counter

s = 'abracadra'
words = ['Donald', 'Mickey', 'Donald', 'Mickey', 'Mickey']

ss = Counter(s)  # Подсчет в виде словаря
ww = Counter(words)
print(ss)
print(ww)

for i in ww.elements():  # Специальный метод (проход по элементам)
    print(i)

print(ww.most_common())  # Вернет пару ключ - значение в порядке частоты появления

print(ww['re'])  # Если такого ключа нету, то вернет 0

new_pr = ['333', 'Mickey', 'Mickey']
pr = Counter(new_pr)
print(ww + pr)  # Можно складывать счетчики Counter()
