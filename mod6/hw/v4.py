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

cur_dir = Path('D:\\TMP')
import os
 
def listdirs(cur_dir):
    list_dirs = []
    for file in os.listdir(cur_dir):
        
        print(file)
        print(type(file))
        d = os.path.join(cur_dir, file)
        if os.path.isdir(d):
            list_dirs.append(d)
            listdirs(d)
    return list_dirs
 
#listdirs(cur_dir)



# List of folders to ignore


def folder_to_ignore(cur_dir, dict_groups):
    list_f = []
    for k in dict_groups:
        list_f.append(Path((cur_dir), str(k)))
    return list_f


def normilize_file_recursion(path):
    # recursion through directories

    for element_path in path.iterdir():
        ext = element_path.suffix
        n_name = normalize(element_path.name.rstrip(ext)) + ext
        if element_path.is_dir() and element_path not in folder_to_ignore(cur_dir, dict_groups):
            target = Path(element_path.parent, normalize(element_path.name))
            if element_path == target:
                normilize_fd_recursion(element_path)  # рекурсія
            else:
                normilize_fd_recursion(d_conflict(element_path, target))
        else:

            print('-')

def d_conflict(element_path, target):
    ext = target.suffix
    try:
        element_path.rename(target)

        # if element_path.is_dir():
        #     print(f'{element_path} >>>: {target}')
        #     element_path.rename(target)
        #     element_path = target 
        #     print(f'{element_path} >>>: ок')
        # elif element_path.suffix.lstrip('.').lower() in dict_groups["archives"]:
        #     print(f'arch: {element_path} >>> {target}')

        #     #shutil.unpack_archive(Path(element_path), str(target).rstrip(ext))
        # else:
        #     print(f'!!!: {element_path} >>> {target}')
        #     #shutil.move(element_path, target)
    except FileExistsError:
            target = Path(str(target) + "_")
            print(f'{element_path} >>> {target}')
            d_conflict(element_path, target)
    finally:
        return(target)


#normilize_fd_recursion(cur_dir)