# Print the count of digits in a no

# 456321 : 6
# 123 : 3
# 7412 : 4

num = int(input("Enter no"))
count =0 
while(num > 0):
    count = count +1
    num = num//10

print("Digit count is : ", count)