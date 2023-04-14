from pathlib import Path
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


# Lists of file extensions to return
ext_unknown = []
ext_no_unknown = []

cur_dir = Path('D:\\TMP1')

# List of folders to ignore


def folder_to_ignore(cur_dir, dict_groups):
    list_f = []
    for k in dict_groups:
        list_f.append(Path((cur_dir), str(k)))
    return list_f
    #     новий шлях до папки
    #     target = Path(element_path.parent, normalize(element_path.name))
    #     # print(f'>>>: {target}')


def fd_rename_and_move(element_path):
    global dict_files_name
    ext = element_path.suffix
    target = None
    n_name = normalize(element_path.name.rstrip(ext)) + ext
    print(f'4. {element_path} is file {element_path.is_file()}')
    if element_path.is_file():
        target = Path(element_path.parent, normalize(element_path.name.rstrip(ext)) + ext)
        for group in dict_groups:
            if element_path.suffix.lstrip('.').lower() in dict_groups[group]:
                dict_files_name[group].append(n_name)
                target = Path(cur_dir, str(group), normalize(element_path.name.rstrip(ext)) + ext)
                dir_to = cur_dir / group
                dir_to.mkdir(exist_ok=True)
    fd_conflict(element_path, target)


def fd_conflict(element_path, target):
    print(f'5 {element_path} is file {element_path.is_file()}')
    
    try:
        # if element_path.is_dir():
        #     print(f'{element_path} >>> {target}')
        #     element_path.rename(str(target))
        # elif element_path.suffix.lstrip('.').lower() in dict_groups["archives"]:
        #     print(f'!розпаковано: {element_path}')
        #     shutil.unpack_archive(Path(element_path), str(target).rstrip(ext))
        # else:
        if element_path.is_file():
            ext = element_path.suffix
            shutil.move(element_path, target)
            #element_path.rename(str(target))
    except FileExistsError:
        if element_path.is_file():
            target = Path(str(target).rstrip(ext) + '_' + ext)
            fd_conflict(element_path, target)

        # if element_path.is_dir():
        #     print(f'{element_path} >>> {target}')
        #     target = Path(str(target) + "_")
        #     fd_conflict(element_path, target)
        # else:
        #     target = Path(str(target).rstrip(ext) + '_' + ext)
        #     fd_conflict(element_path, target)

def parse_folder_recursion(path):
    # recursion through directories
    for element_path in path.iterdir():
        print(f'1. {element_path}')
        if element_path.is_dir() and element_path not in folder_to_ignore(cur_dir, dict_groups):
            print(f'2. {element_path}')
            #fd_rename_and_move(element_path)
            parse_folder_recursion(element_path)  # рекурсія
        else:
            print(f'3. {element_path}')
            fd_rename_and_move(element_path)

parse_folder_recursion(cur_dir)