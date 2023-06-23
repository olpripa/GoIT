# Map

names = ["dan", "jane", "steve", "mike"]

def normalize(name: str):
    return name.title()

new_name = []

# 1
for name in names:
    new_name.append(name.title())
print(new_name)

# 2
new_name = map(normalize, names)
print(list(new_name))

# 3
new_name = map(lambda name: name.title(), names)
print(list(new_name))

# 4
new_name = [name.title() for name in names]
print(new_name)