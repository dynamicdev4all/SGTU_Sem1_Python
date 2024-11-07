# print digits of a number

num = int(input("Enter number"))

while(num > 0):
    # we want unit digits thats y finding rem
    remainder = num % 10
    # print that digit
    print(remainder)
    # decrease the no by removing unit digit
    num = num//10

    # / is used for float division
    #  // is used for integer division
