# String methods.
branch = "    Computer    Science   "
coffee = "Blackcoffee , Americano , Coldcoffee"
name = "Abdul Jabbar"
print(name)

print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.casefold())
print(name.find("Jabbar"))
print(len(name))
for character in name:
    print(character)

print(branch.split())

print(coffee.split(" , "))
print(coffee.replace("Americano","Cappuccino")) 

print("Abdul" in name)
