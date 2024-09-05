# create a dictionary
#  -name
#  -age
#  -roll no

# user input : num 
#   - num is odd
#       then print name
    # -num is even
    #     then print rollno

my_dic = {
    "name" : "Gita",
    "age" : 62,
    "rollno" : 12345
}

num1 = int(input("Enter num"))

# if (conditon)
# even
if num1 % 2 == 0:
    print(my_dic["rollno"])

# odd
# if num1 % 2 == 1:
else:
    print(my_dic["name"])