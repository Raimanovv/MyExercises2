# Напишите программу на Python для сортировки трех целых чисел

listt = list()
while True:
    number = input("number = ")
    if number == '':
        break
    listt.append(int(number))

print(sorted(listt))
