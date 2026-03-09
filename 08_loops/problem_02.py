# Sum of even numbers upto a given number n.
numbers = int(input("Enter the number 'n' : "))
even_num_sum = 0
for num in range(1,numbers+1):
    if num % 2 == 0 :
        even_num_sum += num
print(f"The sum of even numbers upto given n number is : {even_num_sum}")