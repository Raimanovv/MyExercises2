# Напишите программу на Python, чтобы получить разницу между заданным числом и 17,
# если число больше 17, верните двойную абсолютную разницу

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


print(difference(22))
print(difference(14))
