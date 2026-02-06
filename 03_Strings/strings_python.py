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
print(num_list[0:8:2])
print(num_list[-1::-1])
# String methods.
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.casefold())
print(name.find("Jabbar"))
print(len(name))
for character in name:
    print(character)

print(branch.strip())
print(branch.split())

print(coffee.split())
print(coffee.split(" , "))
print(coffee.replace("Americano","Cappuccino")) 

print("Abdul" in name)

# Formatting in string
coffee = "Black coffee"
order = "I oredered one cup of {}."
print(order.format(coffee))

print("Abdul Jabbar \"I am an AIML engineer.\"")

window_path_01 = "C:\\Users\\Abdul Jabbar\\OneDrive\\Desktop"
print(window_path_01)
# ---- OR ----
window_path_02 = r"C:\Users\Abdul Jabbar\OneDrive\Desktop"
print(window_path_02)

# list to string
coffee_vareity = ['Blackcoffee','cappuccino','Coldcoffee']
print(coffee_vareity)
print(" , ".join(coffee_vareity))

