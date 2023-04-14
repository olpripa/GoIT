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
# dict_files_name = {"images": [],
#                     "documents": [],
#                     "audio": [],
#                     "video": [],
#                     "archives": [],
#                     "oter": []}

# Lists of filenames to return
list_images = []
list_documents = []
list_audio = []
list_video = []
list_archives = []
list_other = []

# Lists of file extensions to return
ext_unknown = []
ext_no_unknown = []

#ext = 'rar'
l = list(dict_groups.keys())  # list with destination folders
print(l)

cur_dir = Path('D:\\TMP')

# remove empty directory

def sort_func(path_dir):
    cur_dir = Path(path_dir)
    for file_in in cur_dir.iterdir():
        if file_in.is_dir():
        #     print(f'0: {file.stat().st_size}')
        #     if file.stat().st_size == 0:
        #         print(f'{file.name} is EMPTY directory')
        #         file.rmdir()
            sort_func(path_dir)
        for ext in dict_groups:
            if file_in.suffix.lstrip('.').lower() in dict_groups[ext]:
                #dir_to = cur_dir / ext
                #n_name = normalize(file_in.name.rstrip(ext)) + ext
                #path_out = cur_dir / ext / n_name
                print(f'1: {ext}: {file_in.name}')
                #shutil.move(file_in, path_out)
                #dir_to.mkdir(exist_ok=True)
                #file.rename(dir_img.joinpath(file.name))
                #print(dir_img.joinpath(file.name))

#sort_func (cur_dir)

#print(os.listdir(p))

# Функція перейменовує, переміщає(або розпаковує) файл та повертає нове імя файлу 
def file_rename_and_move(file_in, folder_out='other'):
    
    ext = file_in.suffix
    n_name = normalize(file_in.name.rstrip(ext)) + ext
    path_out = Path(str(cur_dir) + '_', folder_out, n_name)

    if folder_out == 'archives':
        #print(Path(file_in))
        shutil.unpack_archive(Path(file_in), str(path_out).rstrip(ext))
        print(f'unpack to {str(path_out).rstrip(ext)}')
        
    else:
        print(f'move to {path_out}')
        #shutil.move(file_in, path_out)
    return n_name
    
    

# !!!!!!
def chek_extended(file_in):

    global list_images, list_documents, list_audio, list_video, list_archives, list_other
 
    ext = file_in.suffix.lstrip('.')

    if ext in dict_groups.get('images', []):  # this is images
        list_images.append(file_rename_and_move(file_in, 'images'))
        # shutil.move(file_name,'')

    elif ext in dict_groups.get('documents', []):
        list_documents.append(file_rename_and_move(file_in, 'documents'))
    
    elif ext in dict_groups.get('audio', []):
        list_audio.append(file_rename_and_move(file_in, 'audio'))
        
    elif ext in dict_groups.get('video', []):
        list_video.append(file_rename_and_move(file_in, 'video'))
    
    elif ext in dict_groups.get('archives', []):
        list_archives.append(file_rename_and_move(file_in,'archives'))
    else:
        list_other.append(normalize(file_in.name.rstrip(ext)) + ext)
            
    # if ext in dict_groups[]:  # this is know ext
    #     print(dict_groups[ext])
    #     #list_images.append(file_rename_and_move(file_in, 'images'))
    #     # shutil.move(file_name,'')
    # else:
    #     list_other.append(normalize(file_in.name.rstrip(ext)) + ext)

def parse_folder_recursion(path):
    for element in path.iterdir():
        if element.is_dir() and element.name not in dict_groups:
            print(f'parse_folder: This is folder - {element.name}')
            parse_folder_recursion(element)  # рекурсія
        else:
            print('-')
            #print(f'parse_folder: This is file - {element.name}')# ext: {chek_extended(element)}')
            #chek_extended(element)
            
parse_folder_recursion(cur_dir)
# print(f'this is images: {list_images}')
# print(f'this is documents: {list_documents}')
# print(f'this is audio: {list_audio}')
# print(f'this is video: {list_video}')
# print(f'this is archives: {list_archives}')
# print(f'this is unknown extendet: {list_other}')

# print(dict_groups.values())



# all_xlsx_files = list(cur_dir.glob('**/*.xlsx'))
# all_xlsx_files1 = list(cur_dir.glob('*.xlsx'))
# for f in all_xlsx_files1:
#     print(f)
#print(cur_dir.glob('*/**.jpg'))


# for ext in dict_groups:
#     print(ext)
#     print(type(ext))
