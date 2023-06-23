# Map and filter

# 1
nums = [i for i in range(1, 20)]
print(nums)

res = map(lambda x: x ** 2, nums)

result = filter(lambda value: not bool(value % 2), res)  # парні
print(list(result))
# result = filter(lambda value: bool(value % 2), res)  # непарні
# print(list(result))

# 2
result = filter(lambda value: not bool(value % 2), map(lambda x: x ** 2, [i for i in range(1, 20)]))
print(list(result))

# 3
result = map(lambda x: x ** 2, filter(lambda value: not bool(value % 2), [i for i in range(1, 20)]))
print(list(result))
