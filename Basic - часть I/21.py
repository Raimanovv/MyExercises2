# Напишите программу на Python, чтобы выяснить, является ли данное число
# (принять от пользователя) четным или нечетным, распечатайте соответствующее сообщение
# для пользователя.

def chet_or(number):
    return ('Чётное' if number % 2 == 0 else 'Нечётное')


print(chet_or(int(input('Введите число: '))))
