'''
Выводит на экран строки из файла csv
'''

import csv

with open('excel.csv', 'r') as f:
    reader = csv.reader(f)

    for line in reader:
        print(line)  # просто создает списки строк

'''
['name;age;salary']
['Tom;10;4000']
['Sam;19;80000']
'''