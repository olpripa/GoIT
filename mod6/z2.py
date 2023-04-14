def write_employees_to_file(employee_list, path):
    all = []
    fh = open(path, 'w')
    for d in employee_list:
        for e in d:
            all.append(e+'\n')
    str = ''.join(all)
    fh.write(str.rstrip('\n'))
    fh.close()

list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19'], ['Oleksandr Pripa,43', 'Frank Admiral,63','Anna Pripa,16'],['qwerty,34']]
list1 = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19', 'qwerty,10']]
p = 'employee_list.txt'

write_employees_to_file(list1,p)