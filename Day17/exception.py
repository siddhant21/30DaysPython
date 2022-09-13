names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

try:
    #unpacking list
    *nordic_countries, es , ru = names
    print(nordic_countries, es, ru)
except Exception as e:
    print(e)