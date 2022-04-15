# https://stepik.org/lesson/435914/step/3?unit=426037

import json

count_max = 0
id_group = 0

with open('group_people.json') as file:
    data = json.load(file)  # Преобразует json файл
    for i in data:
        count = 0
        id = i['id_group']
        for people in i['people']:
            if people['gender'] == 'Female' and people['year'] - 1977 >= 0:
                count += 1
        if count > count_max:
            count_max = count
            id_group = id

print(id_group, count_max)
