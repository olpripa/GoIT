from pathlib import Path
import sys
import os
import shutil
from normalize import normalize

# with destination folders and known extensions

dict_groups = {"images": ['jpeg', 'jpg', 'bmp', 'gif', 'tiff', 'png'],
               "documents": ['csv', 'doc', 'docx', 'pdf', 'ppt', 'pptx', 'rtf', 'xls', 'xlsx', 'txt'],
               "audio": ['aac', 'amr', 'mp3', 'wav', 'wma', 'wav'],
               "video": ['avi', 'mov', 'mp4', 'mpeg', 'mkv'],
               "archives": ['zip', 'gz', 'tar']}

# Lists of filenames to return
dict_files_name = {"images": [],
                   "documents": [],
                   "audio": [],
                   "video": [],
                   "archives": [],
                   "others": []}


# Lists (set) of file extensions to return
ext_known = set()
ext_unknown = set()

cur_dir = Path('D:\\TMP3')

# List of folders to ignore


def folder_to_ignore(cur_dir, dict_groups):
    list_f = []
    for k in dict_groups:
        list_f.append(Path((cur_dir), str(k)))
    return list_f

# номарлізуємо та переносимо файли по групам
def fd_rename_and_move(element_path):
    global dict_files_name, ext_known, ext_unknown
    target = None

    if element_path.is_dir():
        # Delete empty directory
        if len(os.listdir(element_path)) == 0:
            print(f'4 parse_folder: This is empty folder - {element_path.name}')
            shutil.rmtree(element_path)
            #print(element_path)
            return element_path.parent
        else:
            target = Path(element_path.parent, normalize(element_path.name))
            print(f'5 parse_folder: This is folder - {element_path.name} \n>>> {target}')
            


    if element_path.is_file():
        
        ext = element_path.suffix
        # формуємо шлях призначення
        target = Path(element_path.parent, normalize(element_path.name.rstrip(ext)) + ext)
        unknown = True
        for group in dict_groups:
            if element_path.suffix.lstrip('.').lower() in dict_groups[group]:
                unknown = False
                # Заповнюємо список файлів по групам
                dict_files_name[group].append(normalize(element_path.name.rstrip(ext)) + ext)
                # Заповнюємо множину відомих розширень
                ext_known.add(ext)
                # змінюємо шлях призначення
                target = Path(cur_dir, str(group), normalize(element_path.name.rstrip(ext)) + ext)
                # створюємо папки по групам
                dir_to = cur_dir / group 
                dir_to.mkdir(exist_ok=True)
        if unknown:
            ext_unknown.add(ext)
        print(f'6. parse_folder: This is file {element_path} \n>>> {target}')
    
    return fd_conflict(element_path, target)


def fd_conflict(element_path, target):
    
    try:
        ext = element_path.suffix
        if element_path.is_dir():
            print(f'fd1: {element_path} >>> {target}')
            return element_path.rename(str(target))
        elif element_path.suffix.lstrip('.').lower() in dict_groups['archives']:
            print(f'fd2: {element_path} >>> {target}')
            target_arch = Path(str(target).rstrip(ext))
            shutil.unpack_archive(element_path, target_arch)
            #shutil.rmtree(element_path)
        elif element_path.is_file():
            print(f'fd3: {element_path} >>> {target}')
            shutil.move(element_path, target)
    except FileExistsError:
        if element_path.is_dir():
            print(f'fd4: {element_path} >>> {target}')
            target = Path(str(target).rstrip(ext) + '_')
            #element_path.rename(str(target))
            return element_path.rename(str(target))
            

        elif element_path.is_file():
            print(f'fd5: {element_path} >>> {target}')
            
            target = Path(str(target).rstrip(ext) + '_' + ext)
            fd_conflict(element_path, target)

        
def parse_folder_recursion(path):
    # recursion through directories
    for element_path in path.iterdir():
        
        if element_path.is_dir() and element_path not in folder_to_ignore(cur_dir, dict_groups):
            
            element_path = fd_rename_and_move(element_path)
            parse_folder_recursion(element_path)  # рекурсія
        else:
            
            fd_rename_and_move(element_path)

parse_folder_recursion(cur_dir)