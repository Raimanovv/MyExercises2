# https://stepik.org/lesson/296965/step/1?unit=278693
# Треугольник Паскаля

n = int(input('Ведите число: '))
triangle = []

for i in range(n + 1):
    triangle.append([1] + [0] * n)

for i in range(1, n + 1):
    for k in range(1, i + 1):
        triangle[i][k] = triangle[i - 1][k] + triangle[i - 1][k - 1]

for i in range(0, n + 1):
    for j in range(0, i + 1):
        print(triangle[i][j], end=' ')
    print()

'''
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
'''
