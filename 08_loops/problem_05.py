# Find the first non repeated character.
char = input("Enter the character : ")

for ch in char :
    if char.count(ch) == 1:
        print(f"Non repeated char is : {ch}")