# # Count the odd digits and even digits in a number
# EX : 8523
# odd_digits = 2 (5 and 3)
# even_digitd = 2 (8 and 2)

# ex : 854930
# odd_digits = 3 (5, 3, 9)
# even_digits = 3 (8, 4, 0)

num = int(input("Enter number"))

even_digit = 0
odd_digit = 0
while(num > 0):
    dig = num %10
    if(dig % 2 == 0):
        even_digit = even_digit + 1
    else:
        odd_digit = odd_digit + 1
    num = num//10