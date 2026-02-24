# Coffee Customization
coffee_size = input("Enter the coffee size you wants to enjoy : ")

while True:
    extra_shot_opt = input("Do you want extra shot on your coffee(yes/no) : ").lower()
    if extra_shot_opt in ("yes"):
        extra_shot = True
        break
    elif extra_shot_opt in ("no"):
        extra_shot = False
        break

    else :
        print("invalid input,choose correct option.")


if extra_shot:
    print(coffee_size.capitalize() +" with extar shot,enjoy!")
else:
    print(coffee_size.capitalize() +" Enjoy your coffee.")