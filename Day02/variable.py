"""
Exercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line

Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name

The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.

"""
# 'Day 2: 30 Days of python programming'
import math

first_name = "Mike"
last_name = "Weiler"
full_name = first_name + " " + last_name
country = "U.S"
city = "Hawkins"
age = 11
year =2011
is_married = False
is_true = True
is_light = None

alpha , beta ,gamma =1.1 , 2.2 ,3.3

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))

area_of_circle = math.pi * 30**2
circum_of_circle = math.pi * 30*2

print("without user input (area and circum):--",area_of_circle," ",circum_of_circle)

rad = int(input("enter the radius :")) #input comes as string , i.e need to convert it to integer for usage
area_of_circle = math.pi * rad**2
circum_of_circle = math.pi * rad*2
print(area_of_circle, "   ",circum_of_circle)