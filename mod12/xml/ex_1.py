# pip install pyyaml
import yaml

users = [
    {'name': 'Микола', 'age': 22, 'sex': 'male'},
    {'name': 'Марія', 'age': 22, 'sex': 'female'},
    {'name': 'Назар', 'age': 22, 'sex': 'male'}
]

serialize = yaml.dump(users)
result = yaml.load(serialize, Loader=yaml.FullLoader)
print(result)


with open('test.yaml', 'w', encoding='utf-8') as f:
    yaml.dump({'users': users}, f, allow_unicode=True)


with open('test.yaml', 'r', encoding='utf-8') as f:
    copy_users = yaml.load(f, Loader=yaml.FullLoader)

print(copy_users)