from datetime import datetime

td = '11.04.2023'

d = datetime.strptime(td, '%d.%m.%Y')
print(d.date())
print(d.year)
print(d.month)
print(d.day)

other_d = d.replace(year=2020, month=2, day=29, hour=22, minute=23, second=11)
print(other_d)

str_d = other_d.strftime('%Y/%d/%m %H:%M:%S')
print(str_d)
print(type(str_d))

str_d = other_d.strftime('%d-%m-%Y %H:%M:%S')
print(str_d)
print(type(str_d))

a = datetime.now()

print(a.strftime('%Y, %B %d'))
print(a.strftime('%Y, %b %d'))
print(a.strftime('%d %H %Y'))