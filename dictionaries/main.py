student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSi']}

print(student['name'])
print(student['courses'][0])


student_1 = {1: 'Jack', 'age': 25, 'courses': ['Math', 'CompSi']}
print(student_1[1])


student = {'name': 'Mary', 'age': 25, 'courses': ['Math', 'CompSi']}
student['phone'] = '555-5555'
print(student.get('name'))
print(student.get('phone', 'Not Found'))
student['name'] = 'Jane'
print(student)


student.update({'name':'Luke', 'age':26, 'phone': '324-555'})
print(student)


del student['age']
print(student)

age = student.pop('name')
print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSi'], 'phone': '4545-5656'}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)