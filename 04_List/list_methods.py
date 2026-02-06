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