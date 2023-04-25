import shutil

for shortcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shortcut, description))

# dictionary
employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}


def create_backup(path, file_name, employee_residence):
