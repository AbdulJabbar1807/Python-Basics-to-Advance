branch = "    Computer Science   "
coffee = "Blackcoffee , Americano , Coldcoffee"
name = "Abdul Jabbar"
print(name)

# slicing in strings.
name_first_letter = name[0]
print(name_first_letter)

first_name = name[0:5]
print(first_name)

second_name = name[6:]
print(second_name)

name_last_letter = name[-1]
print(name_last_letter) 

num_list = "0123456789"
print(num_list[:])
print(num_list[0:5])
print(num_list[-1])

# String methods.
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.casefold())
print(name.find("Jabbar"))

print(branch.strip())
print(branch.split())

print(coffee.split())
print(coffee.split(" , "))
print(coffee.replace("Americano","Cappuccino")) 

# Formatting in string
coffee = "Black coffee"
order = "I oredered one cup of {}."
print(order.format(coffee))

# list to string
coffee_vareity = ['Blackcoffee','cappuccino','Coldcoffee']
print(coffee_vareity)
print(" , ".join(coffee_vareity))