# https://www.youtube.com/watch?v=b--R9hY4n1g&list=LL&index=1

import os, shutil


def search():
    for adress, dirs, files in os.walk(input('Введите путь старта\n')):  # Выдает по картежу (путь, [папки], [файлы])
        for file in files:
            if file.endswith('.txt'):  # Если файл заканчивается на '.txt', то True
                yield os.path.join(adress, file)
                '''
                # yield делает из функции объект генератор
                # .join(путь, файл) объединяет пути с учетом операционной системы
                # автоматически добавляет символ '/', если нужно
                '''

for i in search():
    print(i)