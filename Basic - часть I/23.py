#  Напишите программу на Python, чтобы получить n (неотрицательные целые)
#  копии первых 2 символов данной строки. Вернуть n копий всей строки, если длина меньше 2.

def text_editor(word, n):
    return word[:2] * n if len(word) >= 2 else word * n


print(text_editor('Helo', 4))
