print('Thirty ' + 'Days ' + 'Of ' + 'Python')
print('Coding '+ 'For ' + 'All')
company = "Coding For All"
print(company ," " ,len(company))
print(str.upper(company))
print(str.lower(company))
print(company.capitalize())
print(company.title())  
print(company.swapcase())
print(company[7:])
if "Coding" in company : 
    print("true")
print(company.find("Coding"))
print(company.replace('Coding','python'))
print(company.split(" "))
organization = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(organization.split(","))
print(company[0],"\t",company[-1],"\t",company[10])
print(company.find("C"),"\t",company.find("f"),"\t",company.rfind("l"))
print("You cannot end a sentence with because because because is a conjunction".index("because"))
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))
print("You cannot end a sentence with because because because is a conjunction"[31:54]) # slice 
print("Coding For All".startswith('Coding'))
print("Coding For All".endswith('All'))
word_space ='   Coding For All      '
word_space = word_space.strip("   ")
print(word_space)
print("thirty_days_of_python".isidentifier())
ll = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' '.join(ll)
print(result)
line = 'I am enjoying this challenge.'
print(line.split())
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("{}\t{}\t{}\t{}".format("Name","Age","Country","City"))
print("{}\t{}\t{}\t{}".format("Asabeneh","250","Finland","Helsinki"))
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius,area))
print('The area of a circle with radius {} is {}'.format(str(radius), str(area)))