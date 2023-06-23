import csv
# csv.DictReader
# csv.DictWriter

with open('names.csv', 'w', newline='\n') as csvfile:  # newline='\n' - заміна python \n
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'first_name': 'Tom', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Bob', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Terry', 'last_name': 'Bounce'})


with open('names.csv') as file:
    print(file.read())