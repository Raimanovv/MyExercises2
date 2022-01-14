import datetime

d2 = datetime.timedelta(seconds=1234565)  # указать своё время (day=0, seconds=0, minutes=0, hours=0, weeks=0, ...)
print(d2.days)  # без .days выводит 1 day, 0:00:00, а с ним 1 (просто цифра)
print(d2)
