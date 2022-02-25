'''
Если большой файл используем readlines()
Если в пути есть экранирование "/", то используем (r)
'''

with open(r'C:\Users\elina\PycharmProjects\MyExercises\Models\csv\csv.reader().py', encoding='utf-8') as file:
    data = file.read()
    print(data)


''' 
# read
hello world
54
'''