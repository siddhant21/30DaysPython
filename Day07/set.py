# syntax
st = {}
# or
st = set()

it_companies ={'apple','microsoft','oracle','ibm','ibm'}
it_companies.add('twitter')
it_companies.discard('apple')
"""
Diffrence between remove and discard

We can remove an item from a set using remove() method.
If the item is not found remove() method will raise errors,
so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
"""
print(it_companies)

A ={1,2,3}
B ={4,5,3}
print(A.intersection(B)) #intersection
print(A.issubset(B))
print(A.isdisjoint(B))
A = A.union(B) #Joining Sets

print(A)

#symetric difference # it means (A\B)∪(B\A)
print(A.symmetric_difference(B))
del A
