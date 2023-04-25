import os

def total_salary(path):
    open('salary.txt', 'r')
    fh = open(path, 'r')
    line = fh.read().splitlines()
    totl_salary = 0

    for el in line:
        sl = el.split(',')
        totl_salary += float(sl[1])
    
    fh.close()
    return totl_salary     


print(os.getcwd())
print(os.path.abspath('salary.txt'))
#print(total_salary('D:\goit\mod6\salary.txt'))
#print(total_salary("salary.txt"))