# Напишите программу на Python, чтобы получить дату и время создания и изменения файла.

import os.path, time

print(f"Last modified:{time.ctime(os.path.getmtime('62.py'))}")
print(f"Created:{time.ctime(os.path.getctime('62.py'))}")

# os.path.getmtime(path) - время последнего изменения файла, в секундах с начала эпохи
# time.ctime([сек]) - преобразует время, выраженное в секундах с начала эпохи в строку
#                     вида "Thu Sep 27 16:42:37 2012"