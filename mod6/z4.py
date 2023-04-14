def add_employee_to_file(record, path):
    fh = open(path, 'a')
    fh.write(f'\n')
    fh.write(record)
    fh.close()
    

r = 'Pripa Oleksandr,45'
p = 'D:\TMP\employee_list.txt'

add_employee_to_file(r,p)