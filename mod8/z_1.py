# from calendar import monthrange
# from calendar import month
import calendar
from datetime import datetime

# dict_month_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

# td = '11.04.2023'

# d = datetime.strptime(td,'%d.%m.%Y')
# print(d.year)
# print(d.month)
# print(d.day)

# other_d = d.replace(year=2020,month=12)
# print(other_d)

# # Exercise 1
# def get_days_from_today(date):
#     yyyy, mm, dd = date.split('-')

#     date_current = datetime.now()
#     date_in = datetime(year=int(yyyy), month=int(mm), day=int(dd))
#     d = date_current - date_in
#     print(f'beatwin {date_current.date()} and {date_in.date()} is {d.days}')
#     return d.days


# date="1979-11-09"
# get_days_from_today(date)

# # # кількість днів в місяці через monthrange

# # current_year = datetime.now().year
# # month = 3  # int(input())

# # days = monthrange(current_year, month)[1]
# # print(days)

# def year_leap(year):
#     # визначення високосного року
#     if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
#         return True
#     else:
#         return False


# def get_days_in_month(month, year):
#     global dict_month_day
#     # визначення кількості днів у місяці
#     if dict_month_day.get(month) == None:
#         print(f'{month} не корентний номер місяця')
#         return None
#     elif (month == 2) and (year_leap(year) == True):
#         days_m = 29
#     else:
#         days_m = dict_month_day.get(month)
#     print(f'{month} місяць {year} року має {days_m} днів')
#     return days_m

# yy = 2020
# mm = 2

# get_days_in_month(mm,yy)
# # display the calendar
# print(calendar.month(yy, mm))

d = '2021-05-27 17:08:34.149Z'
# print(datetime.fromisoformat('2011-11-04T00:05:23Z'))


def get_str_date(date):

    d1 = datetime.fromisoformat(date)
    return d1.strftime('%A %d %B %Y')


print(get_str_date(d))
