from operator import truediv


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in countries:
    print(i)

for i in names:
    print(i)

for i in numbers:
    print(i)

# Exercises: Level 2

def upper_case(country_string):
        return country_string.upper()
def square(num):
    return num ** 2

list(map(upper_case,countries))
square_nums = list(map(square, numbers))
upper_names = list(map(upper_case, names))

def land(str):
    if 'land' in str:
        return True
    return False

print(list(filter(land, countries)))

def six(string):
    if len(string) == 6:
        return True
    return False

print(list(filter(six, countries)))

def six_or_more(string):
    if len(string) >= 6:
        return True
    return False

print(list(filter(six_or_more, countries)))

def E(string):
    if string[0] == 'E':
        return True
    return False

print(list(filter(E, countries)))
