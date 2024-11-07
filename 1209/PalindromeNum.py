# Check whether a no is palindrome or not
# Palindrome num means:
# Original num == reverse num
# ex : 121 , 252, 6996,1378731

num = int(input("Enter the number"))
# because no will become 0 after divisions thats
# why we have save the copy of the no
num_copy = num
# first i need to find reverse of a number
rev = 0

while(num > 0):
    dig = num%10
    rev = rev*10 + dig
    num = num//10


print("Original num is : ", num)
print("Copied num is : ", num_copy)
print("Reverse num is ", rev)
if(num_copy == rev):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")