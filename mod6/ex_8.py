'''
Створення Диреткорій pathlib
'''
from pathlib import Path

new_dir = Path('ABC')
new_dir.mkdir(exist_ok=True)

new_dir.rmdir()

new_dir = Path('Test/NewFolder/Test/HoHoHo/New')
new_dir.mkdir(exist_ok=True, parents=True)

