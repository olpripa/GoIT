# counter = 0
# while counter < 5:
#     user_input = input(">>> ")
#     counter += 1 
#     if user_input == 'exit':
#         print("Bay, Bay")
#         break
#     else:
#         print(f'You write: {user_input}')

# while True:
#     num = int(input("Enter a number: "))
#     if num > 0:
#         if not num % 2:
#             result = "Positive even number"
#         else:
#             result = "Positive odd number"
#     elif num < 0:
#         result = "Negative number"
#     else:
#         result = "It is zero"
#         print(f"{result}, exit")
#         break
#     print(result)
#
# name = ''
# while True:
#     name = input("PLease enter your name: ") 
#     if name != "Ivan":
#         continue
#     print ("Hello Ivan! Enter Password:")
#     password = input ()
#     if password == '12345':
#         print("Correct")
#         break
#     else:
#         print("Password is not correct, 2")
#         password = input()
#         if password == '12345':
#             print("Correct 2")
#             break
# value = int(input('How matc: '))
# for item in range(value): # range -> 0, 1, 2, 3, 4
#     print (f'Iteration: {item}')
# for index, val in enumerate ('bear', 109):
#     print(index, val)
#     if index == 3:
#         break

# language = 'python'

# match language:
#     case 'c':
#         print('language C')
#     case 'java':
#         print('language JAVA')
#     case 'python':
#         print('language Python')
#     case 'JS':
#         print('language Python')
# 5 ... 55

# string = input('Enter string ')

# count_a = 0 
# count_b = 0
# count_c = 0
# count_symbol = 0
# count_space = 0

# for ch in string:
#     count_symbol += 1
#     if ch == 'a':
#         count_a += 1
#     if ch == 'b':
#         count_b += 1
#     if ch == 'c':
#         count_c += 1
#     if ch == ' ':
#         count_space += 1
# print(f'Symbol: {count_symbol}, a: {count_a}, b: {count_b}, c: {count_c}, space: {count_space}')

#polindrom
#101, 202, 535, 444
# num = int (input('Numbe '))
# n1 = num // 100
# n2 = num % 10

# if n1 == n2:
#     print('Polindrom')
# else:
#     print('No')

# string = input('Рядок: ')

# index = 0

# for char in string:
#     if char == 'a':
#         break
#     index += 1
# print(index)

# if not None:
#     print('Значення не визначене')
# if not 0:
#     print('Це 0')
# if not 0.0:
#     print('Це 0.0')
# if not '':
#     print('пророжній рядок')
# if not []:
#     print('пророжній список')
# if not ():    
#     print('пророжній кортеж')
# if not {}:
#     print('пророжній словник')
# if not set():
#     print('пророжня множина')



# def fun(a, b=2, c=3):
#     return a + b * c


# print(fun(b=4, c=4, a=2))  # 18
# print(fun(c=1, a=2, b=3))  # 5
# print(fun(c=3, b=2, a=7))  # 13


# Обчислюємо факторіал числа n за допомогою рекурсії
# @param n – число, для якого треба розрахувати факторіал
# @return - факторіал числа n


# def factorial(n):
#     if n < 2:
#         return 1  # Базовий випадок
#     else:
#         return n * factorial(n - 1)  # Рекурсивний випадок

# #num = int(input("Введіть додатне ціле число: "))
# n = 50
# k = 7
# def number_of_groups(n, k):
#     return factorial(n) / (factorial(n-k) * factorial(k))

# result = number_of_groups (n,k)
# print(f"Для {n} підписників та {k} призів отримаємо {result} списків")

# first = {'a': 1, 'b': 2, 'c': 3}

# second = {'a': 'New', 'd': 345}

# second.update(first)
# print(second)

# # del second('d')

# print(list(first.keys()))
# print(list(first.values()))
# print(list(first.items()))

# numbers = {0, 4, 5, 3, 7, 4}
# print(numbers)
# print(type(numbers))

# l = [1, 3, 4, 1, 5, 4, 1, 8]
# a = set(l)
# l = list(a)
# print(l)
# print(set('hello'))
# print('o' in a)


# points = {
#     (0, 0): "O",
#     (1, 1): "A",
#     (2, 2): "B"
# }

# print(points)

# from pathlib import *
# current_dir = Path.cwd()
# print(current_dir)
# home_dir = Path.home()
# print(home_dir)

# 'output/output.xlsx'
# import os

# outpath = os.path.join(os.getcwd(), 'output')
# outpath_file = os.path.join(outpath, 'output.xlsx')
# print(outpath_file)

# outpath = Path.cwd() / 'output' / 'output.xlsx'
# print(outpath_file)

# def lookup_key(data, value):
#     list_keys = []
#     for k in data:
#         if data.get(k) == value:
#             list_keys.append(k) 
#     return list_keys

# data = {1: "test", 2:"qwerty", 3:"test"}
# print(lookup_key(data,"test"))

# def split_list(grade):
#     sum_bal = 0
#     list_1, list_2 = [], []
#     if len(grade) == 0:
#         return list_1, list_2
#     else:
#         for i in grade:
#             sum_bal += int(i)
#         middle_b = sum_bal / len(grade)
#         for i in grade:
#             if i <= middle_b:
#                 list_1.append(i)
#             else:
#                 list_2.append(i)
#     return list_1, list_2

# group_a = [56, 75, 88, 95, 50, 80]
# group_b = []
# print(split_list(group_b))
# print(split_list(group_a))


# string = "Метод  1844 fromkeys() класу dict дозволяє створити новий 2244444 словник з послідовності заданих ключів та деякого 3 значення. Згідно з документацією Python 1979 загальна форма використання методу наступна"

# import re
# pattern = r'[0-9]+' # +
# result = re.search(pattern, string)
# print(result.span())
# first_index, last_index = result.span()
# print(string[first_index : last_index])

# result = re.findall(r'\d+',string) #/d == [0-9]
# print(result)
# result = re.findall(r'\d{4}', string)  # /d == [0-9]
# print(result)

# Модуль 5 завдання 1
def real_len(text):
    str_no = ['\n', '\f', '\r', '\t', '\v']
    real_len_text = 0
    for s in text:
        if s in str_no:
            continue
        else:
            real_len_text += 1
    return real_len_text

text = 'Alex\nKdfe23\t\f\v.\r'
text2 = 'Al\nKdfe23\t\v.\r'
print(real_len(text))
print(real_len(text2))

message = "Hello, my little friend. Today is a very good day."
words = message.split(" ")
sentences = message.split(". ")
print(words)
print(sentences)

message = "У темній кімнаті всі кішки чорні (мабуть)"
square_brackets = message.replace("(", "[").replace(")", "]")
clear_brackets = message.replace("(", "").replace(")", "")

print(square_brackets)  # У темній кімнаті всі кішки чорні [мабуть]
print(clear_brackets)  # У темній кімнаті всі кішки чорні мабуть



