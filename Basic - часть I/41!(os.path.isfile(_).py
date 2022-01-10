# Напишите программу на Python, чтобы проверить, существует ли файл.
import os.path


def check_file(path):
    return os.path.isfile(path)


print(check_file('3c4.py'))
