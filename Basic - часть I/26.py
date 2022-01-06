# Напишите программу на Python для создания гистограммы из заданного списка целых чисел.

def histogram(listt):
    return [f'{"*" * (listt[i])}' for i in range(len(listt))]


for i in histogram([2, 3, 6, 5]):
    print(i)
