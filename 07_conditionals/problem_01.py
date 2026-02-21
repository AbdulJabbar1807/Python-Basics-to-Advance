age = input("Enter your age : ")
age_in_int = int(age)

if age_in_int < 13:
    print("You are a Child.")
elif age_in_int < 20:
    print("You are an Teenager.")
elif age_in_int < 60:
    print("You are an Adult.")
else:
    print("You are a Senior.")