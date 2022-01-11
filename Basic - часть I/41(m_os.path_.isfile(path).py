# Напишите программу на Python, чтобы проверить, существует ли файл.
import os.path # является вложенным модулем в модуль os, и реализует некоторые полезные
               # функции для работы с путями

def check_file(path):
    return os.path.isfile(path)


print(check_file('3c4.py'))
