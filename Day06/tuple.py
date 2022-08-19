# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

fruits = ('banana', 'orange', 'mango', 'lemon')

tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items

#tuple to list
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

#deleting tuple
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

#Exercise
"""
We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
"""
tup = ()
tup_list = list(tup)
tup_list.append('brother')
tup_list.append('sister')
tup = tuple(tup_list)
print(tup)
tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1 + tup2
print(tup3,len(tup3))

#unpacking
(bro , sis) = tup
print("unpacking :- ",bro," ",sis)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)