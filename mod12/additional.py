from typing import List
import json

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
# class Team:
#     def __init__(self, students: List[Student]):
#         self.students = students
#
# student_1 = Student('Ivan', 'Tompson')
# student_2 = Student('Igor', 'Smith')
#
# team = Team(students=[student_1, student_2])
# ser_team = json.dumps(team, default=lambda a: a.__dict__, indent=4)
# print(ser_team)
#
# decode_team = Team(**json.loads(ser_team))
# print(decode_team)


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def serialize(self):
        data = json.dumps(self, default=lambda a: a.__dict__)
        return json.loads(data)

    @classmethod
    def deserialize(cls, data):
        return cls(**data)

    def __str__(self):
        return f'{self.first_name}: {self.last_name}. Age: {self.age}'

    def info(self):
        return f'Student({self.first_name}: {self.last_name}. Age: {self.age})'


student_1 = Student('Ivan', 'Tompson', 21)
a = student_1.serialize()
print(a)

d_a = Student.deserialize(a)
print(d_a)
print(d_a.info())