# Напишите программу на Python, чтобы проверить, содержится ли указанное значение
# в группе значений.
# Тестовые данные :
# 3 -> [1, 5, 8, 3]: Верно
# -1 -> [1, 5, 8, 3]: False

def check_list(meaning, listt):
    return f'{meaning} содержится в списке {listt}' if meaning in \
             listt else f'{meaning} не содержится в списке {listt}'


print(check_list(3, [1, 5, 8, 3]))
