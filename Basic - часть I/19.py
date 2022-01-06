# Напишите программу на Python, чтобы получить новую строку из заданной строки,
# где «Is» было добавлено вперед. Если заданная строка уже начинается с «Is»,
# вернуть строку без изменений.

def word_analysis(word):
    if 'is' == word[:2].lower():
        return word
    return f'Is{word}'


print(word_analysis('e'))
