from pathlib import Path

def parse_folder(p):
    files = []
    folders = []
    for i in p.iterdir():
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name.split('.')[0]) #відкидаємо розширення
    return files, folders

p = Path('\ol.pripa\Downloads\Tmp1')  # p Вказує на теку /home/user/Downloads
print(parse_folder(p))