'''
Создать или перезаписать csv своими значениями
лучше использовать ","
'''

import csv

with open('ex.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['row 1 el 1', 'row 1 el 2', 'row 1 el 3'])  # 1-я строка
    writer.writerow(['row 2 el 1', 'row 2 el 2', 'row 2 el 3'])  # 2-я строка
    writer.writerow(['row 3 el 1', 'row 3 el 2', 'row 3 el 3'])  # 3-я строка

'''
row 1 el 1;row 1 el 2;row 1 el 3
row 2 el 1;row 2 el 2;row 2 el 3
row 3 el 1;row 3 el 2;row 3 el 3
'''