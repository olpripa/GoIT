from pickle import loads, dumps

class A:
    x = 'some'
    def __init__(self):
        print('new A!')
        self.y = 'інша змінна'

a = A()
s = dumps(a)
s_class = dumps(A)


restored_a = loads(s)
restored_A = loads(s_class)

print(a.x, a.y)
print(restored_a.x, restored_a.y)
print(restored_A.x)
print(dir(restored_A))