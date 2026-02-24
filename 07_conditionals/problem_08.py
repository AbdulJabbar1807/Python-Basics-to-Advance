# Password strength checker
Password = input("Enter your paswword : ")
Password_length = len(Password)

if Password_length > 10:
    strength = "Strong"
elif Password_length > 6:
    strength = "Medium"
else:
    strength = "Weak"
print(strength)
