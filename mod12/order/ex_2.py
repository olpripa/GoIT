# Друк та нумерація рядків у текстовому файлі.

import pickle

class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, encoding='utf-8')
        self.line_count = 0

    def readline(self):
        self.line_count += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return f'{self.line_count, line}'

    def __getstate__(self):
        state = self.__dict__.copy()
        # Потрібно удалити все що ми не можемо сереліазувати
        del state['file']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.filename, encoding='utf-8')
        for _ in range(self.line_count):
            file.readline()
        self.file = file  # зберігаємо файл

if __name__ == "__main__":
    reader = TextReader('text.txt')
    print(reader.readline())
    print(reader.readline())
    print(reader.readline())
    new_reader = pickle.loads(pickle.dumps(reader))  # повинен запамятати коли він був упакований і продовжити дркувати
        # з того чамого місця
    while True:
        line = new_reader.readline()
        if line is None:
            break
        print(line)
    print('-' * 15)
    print(reader.readline())
    print(reader.readline())
    print(reader.readline())
    print(reader.readline())
    print(reader.readline())
    print(reader.readline())


