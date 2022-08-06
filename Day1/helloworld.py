"""
1.Check the python version you are using

2.Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)

3.Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python


4.Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country

"""

# Python 3.10.2

import math


a=3+2
b=5-4
c=6*7
d=10/2
e=2**3
f=10%3
g=10//3
print(a,b,c,d,e,f,g)

str1='siddhant'
str2='piyush'
str3='India'
str4="I am enjoying 30 days of python"
print(str1,str2,str3,str4)

print(type(10),type(9.8),type(3.14),type(4-4j),type(['Asabeneh', 'Python', 'Finland']),type('siddhant'))

"""
Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
Find an Euclidian distance between (2, 3) and (10, 8)
"""

myint=10
myfloat=3.14
mycomp=2-7j
mystr='siddhant'
mybool=True
mylist=[10,'sid',4-4j]
mytuple=(22,22,4,'sid')
myset={1,2,3}
mydict={'key':'val'}

print(myint,myfloat,mycomp,mystr,mybool,mylist,mytuple,myset,mydict)

# Euclidian distance sqrt((x2-x1)^2 + (y2-y1)^2)   d = √((x2-x1)2 + (y2-y1)2)

euc = math.sqrt((10-2)**2 + (8-3)**2)
print("euc",euc)