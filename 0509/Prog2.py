print("Hi User",end="\t")
name = input("Enter name")
print("Name is : ", name)
print("The type of name is " , type(name))


# age = input("Enter ur age")
# print("The data of age is", type(age))

# the age type was str
# which is not correct

# by default whatever input u take is of type str
# 123 - int
# "123" - str

# i want to make my input of some particylar type

age = float(input("Enter ur age"))
print("The data of age is", type(age))