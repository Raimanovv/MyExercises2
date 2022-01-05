# Напишите программу на Python, чтобы проверить, находится ли число в пределах 100 от 1000
# или 2000.

def near_thousand(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))
