'''
Більше можливостей pathlib
'''
from pathlib import Path

current_path = Path('.')
file = current_path / 'bin' / 'utils' / 'test.svg.io.test'
file = current_path / 'Temp' / 'temp.txt'
print(file.exists())

for el in current_path.glob('*_1*.py'):
    print(el)

for el in current_path.glob('**/*.py'):
    print(el)

tmp = Path('test.txt')
if tmp.exists():
    tmp.unlink()