"""
Метод: find
# Пошук підрядки у рядку. Повертає номер першого входження або -1
# S.find(str, [start], [end])
# Пошук підрядки у рядку. Повертає номер останнього входження або -1
----
Дано рядок символів.
Виключити з цього рядка групи символів між дужками [, ].
Самі дужки теж мають бути виключені.
Передбачається, що в кожній парі дужок немає інших дужок.
"""

string = "Виключити із цієї [рядки групи] символів, [розташовані між] дужками [, ]."

# start_index = string.find('[')  # 18
# end_index = string.find(']')   # 30
# print(start_index)
# print(end_index)
# new_string = string[:start_index] + string[end_index + 1:]  # Виключити із цієї  символів, [розташовані між] дужками [, ].
# print(new_string)

def sanitize(string):
    new_string = string[:]
    while True:
        start_index = new_string.find('[')
        end_index = new_string.find(']')
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index + 1:]
    return new_string


print(sanitize(string))