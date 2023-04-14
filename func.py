# визначення функції
def birthday_card():
    print('Happy birthday!')

# визначення функції
def hungry():
    return True

# визначення функції
def echo(anything):
    return anything

def like(interest):
    if interest == 'yoga':
        return "I quite like " + interest + "."
    elif interest == "football":
        return "Yes, I play " + interest + "."
    elif interest == 'guitar':
        return "Yes, I play the " + interest + "."
    else:
        return "I'm interested in " + interest + "."


def do_nothing():
    pass

def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")

# виклик функції та перевірка умови
if hungry():
    print('Eat oat flakes!')
else:
    print('Drink water.')

print(echo('I enjoy travelling!'))

story = like('photography')
print(story)
story = like('yoga')
print(story)
story = like('football')
print(story)
story = like('guitar')
print(story)

print(do_nothing())

is_none(None)  # It's None
is_none(True)  # It's True
is_none(False)  # It's False
is_none(0)     # It's False
is_none(0.0)   # It's False
is_none(())    # It's False
is_none([])    # It's False
is_none({})    # It's False
is_none(set())  # It's False
