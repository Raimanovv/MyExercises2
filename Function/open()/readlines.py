'''
Если большой файл используем readlines() или readline()
Если в пути есть экранирование "/", то используем (r'')
readlines() - список элементами которого являются строки файлов
'''

with open(r'C:\Users\elina\PycharmProjects\MyExercises\Models\csv\csv.reader().py', encoding='utf-8') as file:
    data = file.read(3)  # Если в скобках указать число 3, то выведет 3 символа
    print(data)
    file.seek(0)  # Откат на 0-ю позицию
    print(file.read(4))  # Курсор остается на последнем символе
