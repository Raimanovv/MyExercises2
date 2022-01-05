# Напишите программу на Python для печати календаря с указанным месяцем и годом.
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))