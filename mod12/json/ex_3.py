import json

data = {
    'developer': {
        'name': 'Іван П.',
        'species': 'Програміст'
    }
}

with open('data_user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)


with open('data_user.json', 'r', encoding='utf-8') as file:
    restore_data = json.load(file)
    print(restore_data)