import csv

with open("excel.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:  # Каждая строка
        print(row)
        print(row['name'], row['salary'], row['age'])
