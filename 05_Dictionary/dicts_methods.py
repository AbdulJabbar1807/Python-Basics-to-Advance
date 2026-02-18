student_info = {"first_name":"Abdul","middle_name":"Jabbar","last_name":"Qureshi"}
print(student_info)
first_name = student_info.get("first_name")
print(f"First name of student is : {first_name}")
print(student_info.get("")) # will give 'None'.

for name_type in student_info:
    print(name_type)
for name_type in student_info:
    print(name_type,student_info[name_type])
for key,value in student_info.items():
    print(key,value)

student_info["father_name"]="Julfikar"
print(student_info)

student_info.popitem()
print(student_info)
del student_info["last_name"]
print(student_info)

student_info_copy = student_info.copy()
student_info["last_name"] = "Qureshi"
print(student_info)
print(f"copy of student first and middle name : {student_info_copy}")