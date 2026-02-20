language = ("Python","Java","C++","Python")
print(language)

subject = ("Science","Maths")
all_sub = language + subject
print(all_sub)

if "Maths" in all_sub :
    print("yes,Maths is there in all subjects.")

print(language.count("Python"))

(a,b,c,d) = language # wrapping a tuple into a tuple.
print(a) # will print "Python"

print(type(all_sub))