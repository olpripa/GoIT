from datetime import datetime

timestamp = 1681837476.915694

date_time = datetime.fromtimestamp(timestamp)
print(date_time)
str_date_time = date_time.strftime('%d-%m-%Y, %H:%M:%S')

str_date = date_time.strftime('%I%p %M:%S')
print(str_date)

print(date_time.weekday())