# Функтор - потрібний коли ми хочимо викликати екземпляр об'єкта як функцію
# Функтор - це коли екземпляр класу може сам себе викликати


class Count:
    def __init__(self, init_steps):
        self.steps = init_steps

    def __call__(self, *args, **kwargs):
        # print(f'args: {args}')
        increment, = args  # args it's a tuple
        self.steps += increment
    # def test(self, value):
    #     self.steps += value

count_step = Count(100)  # є людина, яка біжить і вже пробігла 100 кроків
# count_step.test(25)
# count_step.test(20)
count_step(25)  # пробігла  ще 25 кроків
count_step(20)  # пробігла  ще 20 кроків
print(count_step.steps)

#
count_step_self = Count(40)  # є людина, яка біжить і вже пробігла 40 кроків
count_step_self(11)  # пробігла  ще 11 кроків
count_step_self(33)  # пробігла  ще 33 кроків
print(count_step_self.steps)