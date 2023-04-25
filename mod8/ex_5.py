# Написати функцію, яка визначає який день тижня у певної дати у вигляді "день-місяць-рік".
# '25-04-2023'

from datetime import datetime

days_name = {
   0: "понеділок",
   1: "вівторок",
   2: "середа",
   3: "четвер",
   4: "п'ятниця",
   5: "субота",
   6: "неділя",
}

def day_of_week(date: str):
   day, month, year = date.split('-')
   date = datetime(day=int(day), month=int(month), year=int(year))
   return days_name.get(date.weekday())

print(day_of_week('25-04-2023'))
print(day_of_week('11-01-2023'))
print(day_of_week('25-05-2023'))
print(day_of_week('03-03-2023'))
print(day_of_week('11-11-2023'))