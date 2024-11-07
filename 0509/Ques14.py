# 14.	WAP to create a menu driven program 
# Press 1 for Addition
# Press 2 for Subtraction
# Press 3 for Multiplication
# Press 4 for Division


# - take input : num1 and num2
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

# - display choices
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Enter ur choice")

choice = int(input())
# - choice input


if (choice == 1):
    print(num1 + num2)
elif (choice == 2):
    print(num1 - num2)
elif (choice == 3):
    print(num1 * num2)
elif (choice == 4):
    print(num1 / num2)
else:
    print("Invalid Choice")