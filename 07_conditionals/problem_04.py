# Fruit ripeness checker.
Fruit = input("Enter your fruit name : ")
Fruit_color = input("Enter your fruit color : ")

if Fruit.capitalize() == "Banana":
    if Fruit_color.capitalize() == "Yellow":
        print("Ripe")
    elif Fruit_color.capitalize() == "Green":
        print("Unripe")
    elif Fruit_color.capitalize() == "Brown":
        print("Overripe")
        
if Fruit.capitalize() == "Apple":
    if Fruit_color.capitalize() == "Yellow":
        print("Ripe")
    elif Fruit_color.capitalize() == "Green":
        print("Unripe")
    elif Fruit_color.capitalize() == "Brown":
        print("Overripe")
        
if Fruit != "Banana" or Fruit != "Apple":
    print("Sorry,we dont have any information for that.")