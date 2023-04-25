from datetime import datetime

date = datetime(year=2023, month=4, day=18)
date = datetime(year=2023, month=4, day=18, hour=19, minute=38, second=35)
print(date)
print(type(date))

print(date.date())
print(date.time())

print(datetime.now())
print(datetime.today())

print(date.isoformat())