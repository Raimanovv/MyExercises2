'''
yield возвращает значеии и замораживает вашу функцию
со всеми локальными переменными на этом месте
'''

def genf():
    s = 7
    for i in [43, 65, 32]:
        yield i
        print(s)
        s = s*10+7

g = genf()
print(next(g))
print(next(g))
print(next(g))