"""
Клас datetime.timedelta - різниця між двома моментами часу, з точністю до мікросекунд.
"""
from datetime import datetime, timedelta

# d = datetime.now()
td = '11.04.2023'
interval = timedelta(days=4)
finish_d = td + interval
print(finish_d)