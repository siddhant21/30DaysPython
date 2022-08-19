from ast import Pass


i = 0
while(i<=10):
    print(i)
    i+=1

j = 10
while(j>=0):
    print(j)
    j-=1

for itr in range(0,5):
    for jtr in range(0,itr+1):
        print('#',end='')
    print('\n')

for itr in range(0,5):
    for jtr in range(0,5):
        print('#',end='')
    print('\n')

for itr in range(0,11):
    print('{} X {} = {}'.format(itr,itr,itr*itr))

ls = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in ls:
    print(item)


even_sum = 0
odd_sum  = 0
for it in range(0,101):
    if (it % 2 == 0):
        even_sum = even_sum + it
        print(it) 
for it in range(0,101):
    if (it % 2 != 0):
        odd_sum = odd_sum +it
        print(it) 

total_sum = 0 
for it in range(0,101):
    total_sum = it + total_sum

print(total_sum)    

"""
Exercise 3 based on file handling and conditionals
"""