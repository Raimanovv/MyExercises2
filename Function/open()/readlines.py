'''
Если большой файл
'''

with open('filee.txt') as file:
    data = file.readlines()
    print(data)


''' 
# readlines
['hello world\n', '54'] 

# read
hello world
54
'''