'''
Читання та запис у файл.
'''

file = open('test.txt', 'w', encoding='utf-8')
file.write('Hello world!\n')
file.write('Hello Ukraine!\n')
file.write('Hello Poland!\n')
file.writelines(['Hi Bob\n', 'Hi Ivan\n', 'Hi Gigs\n'])
file.close()

file = open('test.txt', 'r', encoding='utf-8')
# result = file.read()
# result = file.readline()
result = file.readlines()
print(result)
file.close()