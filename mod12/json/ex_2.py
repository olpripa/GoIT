import json

with open('storage.json', 'r') as file:
    storage = json.load(file)

print(storage)
print(storage.get('dict').get('a'))