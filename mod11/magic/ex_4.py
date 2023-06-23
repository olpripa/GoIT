# Методи __getitem__ i __setitem__
from collections import UserList


class PositiveNumber(UserList):
    def __init__(self, data=[]):
        super().__init__()
        self.data = [el for el in list(filter(lambda x: x > 0, data))]

    def __getitem__(self, index):
        if index is None:
            return self.data
        return self.data[index]

    def __setitem__(self, key, value):
        if value > 0 and key < len(self.data):
            self.data[key] = value

    def append(self, item) -> None:
        if item > 0:
            super().append(item)



nums = PositiveNumber([2, -4, 5, 6, -1])
print(nums[None])
print(nums)
print(nums[1])
nums[1] = -2
print(nums)
nums.append(8)
print(nums)
nums.append(-78)
print(nums)