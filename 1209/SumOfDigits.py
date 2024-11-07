# Print sum of all digits of a number
# ex : no is 4568
# 4+5+6+8 = 23
# output : 23

num = int(input("Enter number"))

sum =0
while(num > 0):
    remainder = num % 10
    sum = sum + remainder
    num = num//10

print("Sum of digits is ", sum)
