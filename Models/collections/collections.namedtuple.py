# Класс collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж, с тем дополнением,
# что каждому элементу присваивается имя, по которому можно в дальнейшем получать доступ

from collections import namedtuple

PointV2 = namedtuple('PointV2', 'x y z')

p1 = PointV2(2, 3, 'd')
print(p1.z)

print(p1._asdict())  # Представляет в качестве словаря

p2 = p1._replace(x='Ivan')  # Можно так изменять значения атрибутов
print(p2)
