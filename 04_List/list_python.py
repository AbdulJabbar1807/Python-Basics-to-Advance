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
    print(coffee,end=" ")
print("")
    
# List methods in python.
coffee_type = ['Arabica','Robusta','Liberica']
coffee_type.append("Excelsa")
print(coffee_type)
if "Excelsa" in coffee_type:
    print("Yes,Excelsa is there.")

coffee_type.pop()
print(coffee_type)

coffee_type.remove("Robusta")
print(coffee_type)

coffee_type.insert(1,"Robusta")
print(coffee_type)

#creating a copy of list
coffee_type = ['Arabica','Robusta','Liberica']
coffee_type_copy = coffee_type.copy() # will point to a different reference object in memory.
print(coffee_type)
coffee_type_copy.append("Excelsa")
print(coffee_type_copy)

