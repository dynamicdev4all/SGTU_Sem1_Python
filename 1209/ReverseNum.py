# print reverse of number
# num = 1234
# output = 4321

num = int(input("Enmter no"))
# take initial reverse value 0
rev =0 
while(num > 0):
    # find the last digit
    rem = num%10

    # append the last digit by shifting earlier
    # value by 10
    rev = rev *10 + rem

    # break the num
    num = num//10

print("Reverse of a num is" , rev)