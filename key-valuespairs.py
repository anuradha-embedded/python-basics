student = {'name': 'Anu', 'age': 20, 'major': 'Computer Science'}

# student.update({'name': 'Anuradha', 'age': 24, 'phone': '333-555-4444'})
# student['phone'] = '123-456-7890'
# student['age'] = 22

# print(len(student))  # Output: 3
# print(student.keys())  # Output: dict_keys(['name', 'age', 'major'])
# print(student.values())  # Output: dict_values(['Anu', 20, 'Computer
# age = student.pop('age')

# del student['major']

# print(student['name'])  # Output: Anu
# print(student['age'])   # Output: 20
# print(student.get('name', 'Unknown'))  # Output: Anu
# print(student.get('phone', 'Unknown'))

print(student.items())  

print(student)

for key, value in student.items():
    print(key, value)
# for key in student:
#     print(key, student[key])
# print(age)