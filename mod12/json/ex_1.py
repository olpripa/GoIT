import json

d = {'a': 1}
l = [1, 2.5]
t = (3, 4)
s = 'I am a string!'
b = True
st = {1, 2, 'True'}
print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))
print(json.dumps(b))
# print(json.dumps(st))

obj = {'tuple': t, 'list': l, 'dict': d, 'str': s, 'bool': b, 'None': None}
print(json.dumps(obj))

with open('storage.json', 'w') as f:
    json.dump(obj, f)