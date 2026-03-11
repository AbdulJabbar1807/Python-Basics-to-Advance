# Find the first non repeated character.
char = input("Enter the character : ")

for ch in char :
    print(ch)
    if char.count(ch) == 1:
        print(f"Non repeated char is : {ch}")
        break