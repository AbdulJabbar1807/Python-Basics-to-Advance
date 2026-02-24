# Transportation mode selection.
Distance = float(input("Enter the destinetion(in KM) you want to cover : "))

if Distance > 15:
    transport = "Car"
elif Distance > 2:
    transport = "Bike"
else:
    transport = "Walk"
    
print(f"AI recommends you to use {transport} for your destinetion.")