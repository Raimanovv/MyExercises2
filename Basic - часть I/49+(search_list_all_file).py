# Напишите программу на Python, чтобы вывести список всех файлов в каталоге на Python.

from os import listdir
from os.path import join, isfile


def list_files(path):
    return [i for i in listdir(path) if isfile(join(path, i))]


print(list_files('C:\\aRustam\MyExercises\\Basic - часть I'))
