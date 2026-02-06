#creating a copy of list
coffee_type = ['Arabica','Robusta','Liberica']
coffee_type_copy = coffee_type.copy() # will point to a different reference object in memory.
print(coffee_type)
coffee_type_copy.append("Excelsa")
print(coffee_type_copy)