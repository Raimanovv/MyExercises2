# Напишите программу на Python, чтобы получить абсолютный путь к файлу.

from os.path import abspath
def abs_path(file):
    return abspath((file))

print(abs_path('62.sc'))