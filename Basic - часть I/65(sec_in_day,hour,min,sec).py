# Напишите программу на Python для преобразования секунд в день, час, минуты и секунды.

def sec_convert(sec):
    day = sec // (3600 * 24)
    day_1 = sec % (3600 * 24)
    hour = day_1 // 3600
    hour_2 = day_1 % 3600
    min = hour_2 // 60
    sec = hour_2 % 60
    print('day = ', day)
    print('hour = ', hour)
    print('min = ', min)
    print('sec = ', sec)


sec_convert(1234565)
