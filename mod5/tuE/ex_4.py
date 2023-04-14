"""
Метод: isdigit
----
Заданий список, кожним елементом якого є рядок символів, що складається з одних цифр.
Впорядкувати елементи масиву за зростанням їх числових значень і вивести на екран.
Від максимального елемента відняти значення мінімального та вивести різницю на екран.
Підрахувати середнє значення всіх елементів.
"""

numbers = ["123", "456", "321", "10", "75", "abc", "23c"]

def sanitaze(data):
    result = []
    for el in data:
        if el.isdigit():
            result.append(el)
    return result

def transform_to_numbers(data):
    result = []
    for el in data:
        result.append(int(el))
    return result

nums = sanitaze(numbers)
print(sorted(nums))
nums = transform_to_numbers(nums)
nums.sort()
print(nums)
print(max(nums) - min(nums))
print(sum(nums) / len(nums))