# Напишите программу на Python, чтобы распечатать набор, содержащий все цвета из
# color_list_1, которых нет в color_list_2.
# Тестовые данные :
# color_list_1 = set (["White", "Black", "Red"])
# color_list_2 = set (["Red", "Green"])
# Ожидаемый результат :
# {'Черно-белый'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))
