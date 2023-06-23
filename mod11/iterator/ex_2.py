"""
Реалізуємо ітератор, який виконує ітерацію задану кількість разів по заданій послідовності
"""

class MyIterator:
    def __init__(self, seq, count_loop):
        self.seq = seq
        self.count_loop = count_loop
        self.loop = 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.loop > self.count_loop:
            raise StopIteration
        else:
            value = self.seq[self.index]
            self.index += 1
            if self.index == len(self.seq):
                self.index = 0
                self.loop += 1
            return value

seq = ['Test', 'New', 'Hello']
my_iter = MyIterator(seq, 3)

for el in my_iter:
    print(el, end=' ')

