from pickle import TRUE


age = int(input('Enter your age: '))

if(age>=18):
    print("You are old enough to learn to drive.")
else:
    print("You need {} more years to learn to drive.".format(18-age))


my_age = 22
your_age = int(input('Enter your age: '))

if(my_age == your_age):
    print('we have same age')
elif (my_age < your_age):
    if(your_age-my_age==1):
        print('Age is just a number')
    else:
        print('You are {} years older than me.'.format(your_age-my_age))
else:
    if(my_age-your_age):
        print('Age is just a number')
    else:
         print('I am {} years older than you.'.format(my_age-your_age))


print('compare 2 numbers')
# taking multiple inputs
a,b = input('enter 2 numbers: ').split()
a = int(a)
b = int(b)
print(a , b)
if a==b:
    print('Equal numbers')
elif a<b:
    print('a is smaller than b')
else:
    print('a is greater than b')

def determine_grade(scores):
    if scores >= 80 and scores <= 100:
        return 'A'
    elif scores >= 70 and scores <= 89:
        return 'B'
    elif scores >= 60 and scores <= 69:
        return 'C'
    elif scores >= 50 and scores <= 59:
        return 'D'
    elif scores >= 0 and scores <= 49:
        return 'F'


scores =int(input('enter the score of student: '))
print(determine_grade(scores))

fruits = ['banana', 'orange', 'mango', 'lemon']

print(fruits) if 'apple' in fruits else fruits.append('apple')

"""
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
"""
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    print(person['skills'][((len(person['skills'])-1)//2)])
    print('python' in person['skills'])

if person['is_marred'] ==TRUE:  
    print('Asabeneh Yetayeh lives in Finland. He is married.')