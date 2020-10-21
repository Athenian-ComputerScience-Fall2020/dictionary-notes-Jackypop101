# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  
student = {'name':'Jack', 'age':'15', 'course':['Spanish','Math'], 'sport':'basketball'}
student['phone'] = '555-555-5555'
student['name'] = 'Chen'
student.update({'name':'Hangjie', 'course':['Spanish','US History']})
del student['course']
age = student.pop('age')
print(len(student))
print(student.keys())
print(student.items())
print(student['name'])
print(student.get('phone','not found'))
for key, value in student.items():
    print(key, value)
