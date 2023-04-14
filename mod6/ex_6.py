'''
Основні можливості pathlib
'''
from pathlib import Path

current_path = Path('.')

print(current_path)
print(current_path.cwd())

file = current_path / 'bin' / 'utils' / 'vars' / 'test.svg.io.test'
print(file)
print(current_path.joinpath('bin', 'utils', 'vars', 'test.svg'))

print(file.parts)
print(file.name)
print(file.name.split('.')[0])
print(type(file))
print(file.parent)
print(file.suffix)
print(file.suffixes)