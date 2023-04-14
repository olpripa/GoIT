from glob import glob

from pathlib import Path
import shutil

from normalize import normalize

# with destination folders and known extensions
dict_groups = {"images": ['jpeg', 'jpg', 'bmp', 'gif', 'tiff', 'png'],
               "documents": ['csv', 'doc', 'docx', 'pdf', 'rtf', 'xls', 'xlsx', 'txt'],
               "audio": ['aac', 'amr', 'mp3', 'wav', 'wma', 'wav'],
               "video": ['avi', 'mov', 'mp4', 'mpeg', 'mkv'],
               "archives": ['zip', 'gz', 'tar'],
               "presentations": ['ppt', 'pptx'],
               "oter": []}

cur_dir = Path('D:\\TMP')
