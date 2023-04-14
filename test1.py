# def format_ingredients(ingr):
#     if len(ingr) > 2:
#         ingr.insert(-1, 'and')
#     recept_str = ", ".join(map(str, ingr))
#     return recept_str.replace(', and,', ' and')


# r = ["2 eggs"]
# r_1 = format_ingredients(r)
# print(r_1)

text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh''(song)
'''

string = "out 123 sfrom  32141 [string symbols] 3 in group [test]4   4444 qwery  433 [,]"

def count_digits(string):
    count = 0
    for el in string:
        if el.isdigit():
            count += 1
    return count

print(count_digits(string))

def count_numbers(string):
    count = 0
    pos = 0
    nums = []
    while pos< len(string):
        if string[pos].isdigit():
            num = ''
            while pos < len(string) and string[pos].isdigit():
                num = num + string[pos]
                pos +=1
                nums.append(num)
                count += 1
        else:
            pos +=1
    return count, nums

print(count_numbers(string))

