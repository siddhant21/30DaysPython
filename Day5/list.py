lst = list()
lst = [1,2,3,4,5]
print(len(lst))
print(lst[::2])

lst2=['siddhant',21,"5\'5",'single','jammu']
print(lst2)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
print(it_companies,"\t",len(it_companies))
print("{},{},{}".format(it_companies[0],it_companies[3],it_companies[-1]))
it_companies[-2]='Uber'
print(it_companies)
#Adding in the middle of list
middle=int((len(it_companies))/2)

it_companies = it_companies[:middle] + ["Atlassian"] + it_companies[middle:]
print(str.upper(it_companies[2]))

print('Apple' in it_companies)
it_companies.sort()
it_companies.sort(reverse=True)
print(it_companies.reverse())
print(it_companies)
print(it_companies[3:])
print(it_companies[:-3])
print(it_companies.pop((len(it_companies)-1)//2)) #pop middle element
print(it_companies)
print(it_companies.remove('Atlassian'))
print(it_companies.clear())
## This should give: NameError:
del it_companies
print(it_companies)