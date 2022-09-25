# https://stepik.org/lesson/332555/step/6?auth=login&unit=315943

n = 5

matrix = [[0] * n for _ in range(n)]
i = 1
x = -1
y = 0
d_column = 1  # -1 0 1 столбец
d_row = 0  # -1 0 1 ряд
length = len(str(n ** 2))

while i <= n ** 2:
    if 0 <= d_column + x < n and 0 <= d_row + y < n and matrix[d_row + y][d_column + x] == 0:
        x += d_column
        y += d_row
        matrix[y][x] = i
        i += 1

    else:
        if d_column == 1:
            d_column = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_column = -1
        elif d_column == -1:
            d_column = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_column = 1

for row in matrix:
    for elem in row:
        print(str(elem).rjust(length), end=' ')
    print()
