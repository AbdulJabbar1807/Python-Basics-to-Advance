# Validate input : keep asking the user for an input until they enter a number between 1 and 10.
while True:
    number = int(input("Enter the number b/w 1 and 10 : "))
    if  1 <= number <= 10:
        break
    else:
        print("Reenter the number!")
    
print("your number is : ",number)