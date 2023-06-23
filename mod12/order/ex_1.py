# Реалізувати pickable клас, який зберігає дату та час коли об'єкт цього класу серіалізували та коли десеріалізували.

import pickle
from time import sleep
from datetime import datetime

class RememberAll:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        state = self.__dict__.copy()  # __dict__ - тут зберігаються всі властивості класу (поля, методи)
        # print(state)
        state['saved'] = datetime.now()  # змінюємо значення по ключу. state - це є словник
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)  # все що в ньому було замінюємо на state, що прийшов
        self.restored = datetime.now()


if __name__ == '__main__':
    r = RememberAll(1, 2, 3, 4, 5)
    print(r.data)
    r_dump = pickle.dumps(r)
    sleep(5)
    r_load = pickle.loads(r_dump)
    print(r.saved, r.restored)
    print(r_load.saved, r_load.restored)
