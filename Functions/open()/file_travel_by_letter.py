with open(r'C:\Users\elina\PycharmProjects\MyExercises\Models\csv\excel.csv', encoding='utf-8') as file:
    for row in file:  # Вывод построчно (после каждой строки отступ) (Функция print() по умолчанию добавляет в концу вывода символ перенос строки и считанная строка из файла имеет в конце символ перенос строки)
        for letter in row:  # Вывод побуквенно
            print(letter)
