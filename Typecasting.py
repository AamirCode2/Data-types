name = "penguin"
age = 15
is_student = True
weight = 38.5

print("Name :", name)
print("Data type of name is:", type(name))

print("Name :", is_student)
print("Data type of name is:", type(is_student))

print("Name :", age)
print("Data type of name is:", type(age))

print("Name :", weight)
print("Data type of name is:", type(weight))

print("\nAfter type casting...")
age = str(age)
print(age)
print("Data type of age is now:", type(age))
weight = int(weight)
print(weight)
print("Data type of weight is now:", type(weight))