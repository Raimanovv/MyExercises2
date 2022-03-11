# Примеры работы с lambda

nn = list(range(10))
print(list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, nn))))
