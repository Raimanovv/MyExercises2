class Car:
    model = 'BMW'
    engine = 1.6


print(Car.__dict__)  # Можно смотреть все атрибуты, которые существуют в классе ('__'не интересуют)
print(getattr(Car, 'xx', 100))  # Если атрибута 'xx' нету, то выводит '100'. Атрибут указывактся в ''
print(Car.engine)

Car.x = 'error'  # Изменение значения атрибута, если такого атрибута нету, то питон сам создаст новый!
# setattr(Car, 'x', 'error')  -  то же самое
print(Car.x)

del Car.engine  # Удаляет атрибут
# delattr(Car, 'engine')  -  то же самое что и del
