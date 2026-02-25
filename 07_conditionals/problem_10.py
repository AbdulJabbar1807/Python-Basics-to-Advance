# Pet food Recommendation
pet_name = input("Enter your pet type : ").lower()
pet_age = int(input("Enter pet age : "))

if pet_name == "dog" and pet_age < 2:
    print("Puppy food.")
elif pet_name == "cat" and pet_age > 5:
    print("Senior cat food.")