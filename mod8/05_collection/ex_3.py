"""
defaultdict
collections.defaultdict нічим не відрізняється від звичайного словника за винятком того, що за замовчуванням завжди викликається функція, що повертає значення:
"""
from collections import defaultdict

# {key: [], key2: []}
data_d = defaultdict(list)
data_d[0].append(10)
data_d[0].append(4)
data_d[0].append(15)

data_d[1].append(150)
data_d[1].append(3)

data_d['test'].append(45)
data_d['test'].append(1)
print(data_d)

colors = [('yellow', 1), ('blue', 3), ('red', 11), ('yellow', 1), ('red', 1)]
colors_d = defaultdict(list)
for key, value in colors:
    colors_d[key].append(value)
print(colors_d)