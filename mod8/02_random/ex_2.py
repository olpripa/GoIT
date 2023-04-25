import random
l = list(range(1, 37))
print(l)

random.shuffle(l)
print(l)
print(random.choice(l))
new_list = random.sample(l, k=11)
print(new_list)
