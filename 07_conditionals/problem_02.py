#Movie ticket pricing
age = int(input("Enter your age : "))
day = input("Enter the day : ")

price = 12 if age >= 18 else 8
if day.capitalize() == "Wednesday":
    price -= 2
    
print(f"Your ticket price is ${price}")