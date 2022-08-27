import statistics as stat
def add_two_numbers(a,b):
    return a+b
def area_circle(r):
    return 3.14*r*r
def add_all_nums(value):
    if type(value)!=list:
        return "not a list format"
    sum = 0
    for it in value:
        sum = sum+it
    return sum
def convert_celsius_to_fahrenheit(C):
    f =  C * (9/5)  + 32
    return f
def check_season(month):
    Winter = ['NOV','DEC','JAN','FEB']
    Autumn = ['SEPT','OCT']
    Spring = ['MAR','APR']
    Summer = ['JUN','JUL','AUG']

    if month in Winter:
        print('winter season')
    elif month in Autumn:
        print('autumn season')
    elif month in Spring:
        print('spring season')
    else:
        print('summer season')
def solve_quadratic_eqn(a,b,c):
    # ax² + bx + c = 0
    x1=(-b + (b**2 -4*a*c)**1/2)/2*a
    x2=(-b - (b**2 -4*a*c)**1/2)/2*a
    return (x1,x2)
def print_list(ls):
    for it in ls:
        print(it)
def reverse_list(ls):
    return ls.reverse()
def capitalize_list_items(ls):
    for i in range(len(ls)):
        ls[i] = ls[i].upper()
    return ls
def add_item(ls,item):
    ls.append(item)
def remove_item(ls,item):
    ls.remove(item)
def sum_of_numbers(num):
    sum=0
    for i in range(num+1):
        sum = sum + i 
    return sum
def sum_of_odds(num):
    sum=0
    for i in range(num+1):
        if i%2!=0:
            sum = sum + i 
    return sum
def sum_of_even(num):
    sum=0
    for i in range(num+1):
        if i%2==0:
            sum = sum + i 
    return sum
def evens_and_odds(num):
    even = 0
    odd  = 0
    for i in range(num+1):
        if i%2==0:
            even = even + 1
        else:
            odd = odd + 1
def factorial(num):
    factorial = 1    
    if num < 0:    
        print(" Factorial does not exist for negative numbers")    
    elif num == 0:    
        print("The factorial of 0 is 1")    
    else:    
        for i in range(1,num + 1):    
            factorial = factorial*i 
    return factorial
def is_empty(itrable):
    if itrable.size()==0:
        return True
    return False
def mean(ls):
    return stat.mean(ls)   
def median(ls):
    return stat.median(ls)  
def mode(ls):
    return stat.mode(ls)
def std(ls):
    return stat.stdev(ls)  
def var(ls):
    return stat.variance(ls)