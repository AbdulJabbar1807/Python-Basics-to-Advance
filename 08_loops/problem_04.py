# Reverse a string using loops.
input_string = input("enter the string you wants to reverse : ")
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string
    print(reversed_string)# demonstrating each step print.
    
print(f"Reversed string is : {reversed_string}")

    