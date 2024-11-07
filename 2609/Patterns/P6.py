n = int(input("Enter value"))
for i in range(n,0,-1):
    print(" "* (n-i) , end="")
    print("*" * i)
