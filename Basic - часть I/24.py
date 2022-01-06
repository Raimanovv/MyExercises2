# Напишите программу на Python, чтобы проверить, является ли пропущенная буква гласной или нет.

def check_letter(letter):
    return 'Гласная буква' if letter in 'ауоиэыяюеё' else 'Согласная буква'


print(check_letter('е'))
