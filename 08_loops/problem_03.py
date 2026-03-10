# Multiplication table printer
number = int(input("Enter the number for multiplication table : "))

for i in range(1,11):
    if i == 5: # skip the fifth iteration.
        continue
    print(f"{number} x {i} = {number*i}")
    print(end="")
    