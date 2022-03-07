# https://www.youtube.com/watch?v=b--R9hY4n1g&list=LL&index=1
# Поиск по всем файлам '.txt' и копирование в определенное место

import os, shutil

KEY_FOR_SEARCH = input('Что ищем???\n')  # Константы пишутся под импортом
PATH_FOR_COPY = input('Куда копировать файлы?\n')


def search():
    for adress, dirs, files in os.walk(input('Введите путь старта\n')):  # Выдает по картежу (путь, [папки], [файлы])
        if adress == PATH_FOR_COPY: # Исключает возможность парсинга скопированных файлов
            continue  # Начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)
        for file in files:
            if file.endswith('.txt') and '$' not in file:  # Если файл заканчивается на '.txt', то True
                yield os.path.join(adress, file)
                '''
                # yield делает из функции объект генератор
                # .join(путь, файл) объединяет пути с учетом операционной системы
                # автоматически добавляет символ '/', если нужно
                '''


def read_from_pathtxt(path):
    with open(path) as r:  # Если не указать в '', то автоматически используется 'r'
        for i in r:  # Построчное чтение файла, для экономии рабочей мощности компьютера
            if KEY_FOR_SEARCH in i:
                return copy(path)
                # Функция будет завершать свою работу с помощью return,
                # выдавать значение и одновременно с этим запускать функцию copy()
                # передавая в нее path


def copy(path):
    file_name = path.split('\\')[-1]  # Путь делим по символу '\' и из полученного списка берем последний элемент
    # Это имя файла с расширением
    count = 1
    while True:
        if os.path.isfile(os.path.join(PATH_FOR_COPY, file_name)):  # Проверяет существует ли по такому пути к-т файл
            if f'({count - 1})' in file_name:  # Если мы уже создавали такой файл, то True
                file_name = file_name.replace(f'({count - 1})', '')  # Удаляет ненужное число в ()
            file_name = f'({count}).'.join(file_name.split('.'))
            # Объединяет добавленный счетчик в '().' с помощью '(count).' после разделения по '.'
            count += 1
        else:
            break

    shutil.copyfile(path, os.path.join(PATH_FOR_COPY, file_name))  # os.path.join(Путь, ИмяНовогоФайлаКудаКопируем)
    # shutil.copyfile(ПутьГдеЛежитОригинал, Путь'\'ИмяНовогоФайлаКудаКопируем)

    print('Файл скопирован', file_name)


for i in search():
    try:
        read_from_pathtxt(i)
    except Exception as e:
        with open(os.path.join(PATH_FOR_COPY, 'errors.txt'), 'a') as r:  # Указываем, где создаем файл open((тут), 'a')
            r.write(f'{str(e)}\n{i}\n')
