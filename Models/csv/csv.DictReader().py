'''
Прочитать определенные столбцы csv
'''

import csv

with open("excel.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:  # Каждая строка в виде словаря
        print(row['name'], row['salary'], row['age'])

'''
Tom 4000 10
Sam 80000 19
'''