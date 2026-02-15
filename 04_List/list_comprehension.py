# list comrehension in python
square_num = [x**2 for x in range(10)]
print(square_num)
cube_num = [y**3 for y in range(10)]
print(cube_num)

raw_data = "  abdul ,  SAliM,   jOhn  ,  mArYam  "
filtered_data = [filtered.strip().capitalize() for filtered in raw_data.split(",")]
print(filtered_data)

fruits = "apple#banana#cherry#orange"
filtered = [fruit.strip().upper() for fruit in fruits.split("#")]
print(filtered)