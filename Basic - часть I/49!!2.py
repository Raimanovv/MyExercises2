# Напишите программу на Python, чтобы вывести список всех файлов в каталоге на Python.

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('C:\\aRustam\MyExercises') if isfile(join('C:\\aRustam\MyExercises', f))]
print(files_list)