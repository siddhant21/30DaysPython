"""
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

"""
import math

age = 21
height = 5.5
comp = 4 + 6j

triangle_height = int(input("enter height of triangle:"))
triangle_base = int(input("enter triangle base"))
print(0.5*triangle_base*triangle_height) #area of triangle

a=int(input('side 1 of triangle:'))
b=int(input('side 2 of triangle:'))
c=int(input('side 3 of triangle:'))
print("perimeter of triangle",a+b+c)

rectangle_length = 10
rectangle_breadth = 8
print("area rectangle",rectangle_length * rectangle_breadth)
print("perimeter rectangle",2*rectangle_length*rectangle_breadth)

print("area of circle",math.pi*5*5)
print("perimeter of circle",math.pi*5*2)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
# x-intercept, put (y=0)  0 = 2x - 2    ==> [x = 1]   
# y-intercept, put (x=0)  y = 2(0) - 2  ==> [y = -2]

if(len('python')) == (len('dragon')):
    print('true')

if 'on' in 'python' and 'dragon':
    print("present")

if 'jargon' in 'I hope this course is not full of jargon' :
    print('jargon present')

int_python = len('python')
float_python = float(int_python)
string_python = str(float_python)

print(int_python ,float_python,string_python)

num = 10
if (num % 2) == 0:
    print("even")
else :
    print("odd")

hours = 40
rate_per_hour = 28
print("per week earning",hours*rate_per_hour)

print("person can live",31536000*100)

# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1,6):
    print(i,"\n")
    for j in range(4):
        print(i**j,end=" ")
 
