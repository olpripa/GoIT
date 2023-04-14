# Завдання 
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

#Lists of filenames to return
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

# тестування функції
# list_fol = folder_to_ignore(cur_dir, dict_groups)

# element_path = Path('D:\\TMP\\AUDIO\\IMAGES')

# if element_path in folder_to_ignore(cur_dir, dict_groups):
#     print(element_path)
# else:
#     print('!!!!!')


def is_emptydirectory(dir):
    pass

# emptydirectory = Path('D:\\TMP\\Empty')
# #nonemptydirectory = Path('D:\\TMP\\Сад')
# f = Path('D:\\ol.pripa\\Documents\\GitHub\\Si прайс для імпорту.xlsx')
# #print(len(os.listdir(nonemptydirectory))) # 1
# print(len(os.listdir(emptydirectory))) # 0
# #target = Path(nonemptydirectory.parent, normalize(nonemptydirectory.name))
# ext = f.suffix
# n_name = normalize(f.name.rstrip(ext)) + ext

# target = Path(f.parent, n_name)
# print(target)

# try:
#     print(nonemptydirectory.rename(target))
# except FileExistsError:
#     target = Path(str(target) + "_")
#     print(nonemptydirectory.rename(target))

# # Delete empty directory
# if len(os.listdir(element_path)) == 0:
#     print(f'parse_folder: This is empty folder - {element_path.name}')
#     #shutil.rmtree(element_path)
#     continue



def parse_folder_recursion(path):
    # recursion through directories
    for element_path in path.iterdir():
        
        if element_path.is_dir() and element_path not in folder_to_ignore(cur_dir, dict_groups):
            fd_rename_and_move(element_path)
            parse_folder_recursion(element_path)  # рекурсія
        else:
            pass
            #fd_rename_and_move(element_path)
            # ext: {chek_extended(element_path)}')
            #chek_extended(element_path)


def fd_rename_and_move(element_path):
    global dict_files_name
    ext = element_path.suffix
    target = None
    path_out = None
    n_name = normalize(element_path.name.rstrip(ext)) + ext

    #print(element_path)

    if element_path.is_dir():
        target = Path(element_path.parent, normalize(element_path.name))
        #print(f'>>>: {target}')
        
    else:
        target = Path(element_path.parent, normalize(element_path.name.rstrip(ext)) + ext)
        
        for group in dict_groups:
            if element_path.suffix.lstrip('.').lower() in dict_groups[group]:
                dict_files_name[group].append(n_name)
                
                target = Path(cur_dir, str(group), normalize(element_path.name.rstrip(ext)) + ext)
                dir_to = cur_dir / group
                dir_to.mkdir(exist_ok=True)
                
            
        #         path_out = Path(cur_dir, ext, n_name)
        #         #print(path_out)
        #         #if archives - file unpack
        #         if ext == "archives":
        #             print(f'parse_folder: - {element_path.name} | {n_name}')
        #             #shutil.unpack_archive(Path(element_path), str(path_out).rstrip(ext))
        #         else:
        #             print(f'parse_folder: {ext} - {element_path.name} | {n_name}')
        #             dir_to = cur_dir / ext
        #             dir_to.mkdir(exist_ok=True)
        #             #shutil.move(element_path, path_out)

        #  else:
        #      # List of files in category
        #      dict_files_name['others'].append(element_path.name)
        # print(f'>>>: {target}')
        # print(f'!!!: {path_out}')
        fd_conflict(element_path, target)


def fd_conflict(element_path, target):
    ext = target.suffix
    try:
        if element_path.is_dir():
            print(f'{element_path} >>> {target}') 
            element_path.rename(target)
        elif element_path.suffix.lstrip('.').lower() in dict_groups["archives"]:
            print(f'!розпаковано: {element_path}')
            shutil.unpack_archive(Path(element_path), str(target).rstrip(ext))
        else:
            
            shutil.move(element_path, target)
    except FileExistsError:
        if element_path.is_dir():
            print(f'{element_path} >>> {target}')
            target = Path(str(target) + "_")
            fd_conflict(element_path, target)
        else:
            target = Path(str(target).rstrip(ext) + '_' + ext)
            fd_conflict(element_path, target)


    
        
             
        
            
                 

#parse_folder_recursion(cur_dir)

# виводимо список
# for ext in dict_files_name:
#     print(f'{ext}: {dict_files_name[ext]}')
