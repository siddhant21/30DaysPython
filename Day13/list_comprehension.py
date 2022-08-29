numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
new_numbers = [i for i in numbers if i>=0]
print(new_numbers)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
new_list_of_list = [item for i in list_of_lists for j in i for item in j]
print(new_list_of_list)

def list_of_tuples():
    list_of_tupes = []
    for i in range(11):
        list_of_tupes.append((i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5))
    return list_of_tupes

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries_list = [[item[0].upper(), item[0].upper()[:3], item[1].upper()] for it in countries for item in it]

def list_to_list_dict():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    countries = [[sub2[0].upper(), sub2[1].upper()] for sub in countries for sub2 in sub]
    countries = [x for sub in countries for x in sub]
    keys = ["country", "city"]
    return [{keys[0]: countries[idx], keys[1]: countries[idx + 1]} for idx in range(0, len(countries), 2)]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name_list = [x for sub in names for sub2 in sub for x in sub2]
concat_val = [[name_list[0]+ '' +name_list[1]] for i in range(0,len(name_list),2)]

