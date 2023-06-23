import pickle

d = {"some key": 12345}
with open('my_dict.bin', 'wb') as f:
    pickle.dump(d, f)  # записує сереалізований обєкт у файл. Файл буде бінарним


d_bytes = pickle.dumps(d)
print(d_bytes)

with open('my_dict.bin', 'rb') as file:
    db = pickle.load(file)

print(db)
print(pickle.loads(d_bytes))


# dump i load # для роботи з файлами
# dumps i loads # для передачі по мережі