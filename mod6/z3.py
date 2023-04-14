def read_employees_from_file(path):
    fh = open(path, 'r')
    list_employees = fh.read().splitlines()
    fh.close()
    return list_employees


p = 'D:\TMP\employee_list.txt'
print(read_employees_from_file(p))