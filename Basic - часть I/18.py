# Напишите программу на языке Python для расчета суммы трех заданных чисел, если
# значения равны, тогда верните трижды их сумму.

def function(a, b, c):
    sum = a + b + c
    if a == b == c:
        sum *= 3
    return sum


print(function(10, 10, 10))
