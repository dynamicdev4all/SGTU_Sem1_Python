# create a dictionary
#  -name
#  -age
#  -roll no

my_dictionary = {
    "name": "Rohan",
    "age": 20,
    "roll_no": 12345
}

# user input : num 
num  = int(input("Enter the num"))


#   - num is odd
#       then print name
# if num % 2 ==1

if num % 2 != 0 : 
    print(my_dictionary["name"])