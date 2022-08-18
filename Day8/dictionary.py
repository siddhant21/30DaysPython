"""
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
"""
dog = {}
dog ={
    'name':'bruno',
    'color':'brown',
    'breed':'german-shephod',
    'legs':4,
    'age':6
}
print(dog)

student = {
    'first_name':'rob',
    'last_name':'martin',
    'gender':'male',
    'age':12,
    'marital status':'unmarried',
    'skills':['sportsPerson','coder','dancer'],
    'country':'India',
    'city':'delhi',
    'address':'xyz delhi'
}
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('singer')
print(student['skills'])
keys = student.keys()
items = student.items()
print(keys)
print(items)
student.pop('first_name')
del student
