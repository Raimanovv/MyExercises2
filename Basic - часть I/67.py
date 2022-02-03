# Напишите программу на Python для преобразования давления в килопаскалях в кгс на
# квадратный см, миллиметр ртутного столба (мм рт. Ст.) И атмосферное давление.


def translate(number):
    print(f'{number}кПа = {round(number * 0.00980665, 2)}кгс/см2')
    print(f'{number}кПа = {round(number * 7.5006156, 2)}мм рт. Ст.')
    print(f'{number}кПа = {round(number * 0.00986923, 2)}атм')


translate(float(input('Введите число кПа: ')))
