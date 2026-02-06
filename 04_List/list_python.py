coffee_type = ['Arabica','Robusta','Liberica']
print(coffee_type)
print(coffee_type[0])
print(coffee_type[0:2])

coffee_type[2] = 'Excelsa'
print(coffee_type)

print(coffee_type[1:2])# will provide string at index 1 in list.
coffee_type[1:2] = 'Liberica'# will place Liberica at index 1 in list but with each character separeted by ", ".
print(coffee_type)
coffee_type[0:1] = 'Arabica'
print(coffee_type)

coffee_type[0:2] = ['Arabic','Liberica'] # both values will be treated as an array elements
print(coffee_type)

coffee_type = ['Arabica','Robusta','Liberica']
print(coffee_type)

print(coffee_type[1:1])
coffee_type[1:1] = ['beans','beans','beans']
print(coffee_type)
print(coffee_type[1:2])
print(coffee_type[2])
coffee_type[1:4] = [] # deletion operation
print(coffee_type)

# for loop in python
coffee_type = ['Arabica','Robusta','Liberica']
for coffee in coffee_type:
    print(coffee)
for coffee in coffee_type:
    print(coffee,end=",")