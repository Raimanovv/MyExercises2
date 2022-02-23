import csv

with open('excel.csv', 'r') as f:
    reader = csv.reader(f)

    for line in reader:
        print(line)  # просто создает списки строк
