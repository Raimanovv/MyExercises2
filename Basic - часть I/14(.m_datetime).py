# Напишите программу на Python для расчета количества дней между двумя датами.
# Даты выборки : (2014, 7, 2), (2014, 7, 11)
# Ожидаемый выход : 9 дней

from datetime import date

f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
