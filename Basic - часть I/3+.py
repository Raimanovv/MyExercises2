#Напишите программу на Python для отображения текущей даты и времени.

import datetime
now = datetime.datetime.now()
print ("Current date and time: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
