# Копирует все фото '.jpg'

import os, shutil

PATH_FOR_COPY = input('Куда копировать файлы?\n')


def search():
    for adress, dirs, files in os.walk(input('Введите путь старта\n')):  # Выдает по картежу (путь, [папки], [файлы])
        if adress == PATH_FOR_COPY:  # Исключает возможность парсинга скопированных файлов
            continue  # Начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)
        for file in files:  # Из [файлы]
            if file.endswith('.jpg'):  # Если файл заканчивается на '.txt', то True
                yield os.path.join(adress, file)
                '''
                # yield делает из функции объект генератор
                # .join(путь, файл) объединяет пути с учетом операционной системы
                # автоматически добавляет символ '/', если нужно
                '''


def copy(path):
    file_name = path.split('\\')[-1]  # Путь делим по символу '\' и из полученного списка берем последний элемент
    # Это имя файла с расширением

    shutil.copyfile(path, os.path.join(PATH_FOR_COPY, file_name))  # os.path.join(Путь, ИмяНовогоФайлаКудаКопируем)
    # shutil.copyfile(ПутьГдеЛежитОригинал, Путь'\'ИмяНовогоФайлаКудаКопируем)

    print('Файл скопирован', file_name)


for i in search():
    try:
        copy(i)
    except Exception as e:
        with open(os.path.join(PATH_FOR_COPY, 'errors.txt'), 'a') as r:  # Указываем, где создаем файл open((тут), 'a')
            r.write(f'{str(e)}\n{i}\n')
