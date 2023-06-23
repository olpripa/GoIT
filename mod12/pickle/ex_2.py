import pickle

FILENAME = 'users.dat'
users = [
    ['Ivan', 16, True],
    ['Ira', 21, True],
    ['Igor', 25, False],
]

with open(FILENAME, 'wb') as file:
    pickle.dump(users, file)

with open(FILENAME, 'rb') as file:
    user_from_file = pickle.load(file)
    for user in user_from_file:
        print('Name:', user[0], '\tAge:', user[1], '\tStatus:', user[2])
