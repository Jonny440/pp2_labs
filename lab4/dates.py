#Dates
#1
import datetime

today = datetime.datetime.today()
diveDays = today - datetime.timedelta(days=5)

print(diveDays.strftime('%d'))

#2
import datetime

today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)

print(yesterday)
print(today)
print(tomorrow)

#3
import datetime

today = datetime.datetime.today()

print(today.strftime("%Y-%m-%d %H:%M:%S"))

#4
import datetime

date1 = datetime.datetime(2025, 2, 11, 12, 54, 2)
date2 = datetime.datetime(2025, 1, 20, 15, 22, 22)
diff = date1 - date2

print(diff.total_seconds())