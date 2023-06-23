import pickle
from time import sleep
from datetime import datetime


class RememberAll:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        # __dict__ - тут зберігаються всі властивості класу (поля, методи)
        state = self.__dict__.copy()
        # print(state)
        # змінюємо значення по ключу. state - це є словник
        state['saved'] = datetime.now()
        return state

    def __setstate__(self, state):
        # все що в ньому було замінюємо на state, що прийшов
        self.__dict__.update(state)
        self.restored = datetime.now()


if __name__ == '__main__':
    r = RememberAll(1, 2, 3, 4, 5)
    print(r.data)
    r_dump = pickle.dumps(r)
    sleep(1)
    r_load = pickle.loads(r_dump)
    print(r.saved, r.restored)
    print(r_load.saved, r_load.restored)
filter()
