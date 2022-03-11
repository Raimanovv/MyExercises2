# Пример работы с lambda

# аналог def
# можно писать все, что допустимо после return в def
# не выполняется до вызова ()
# можно писать без лямбд

nn = list(range(10))
print(list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, nn))))

# Можно заменить на ...

#print(list(i ** 2 for i in nn if i % 2 == 0))
