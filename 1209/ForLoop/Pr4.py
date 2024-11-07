# WAP to print fizzbuzz (no div by 5 and 7)
# buzz(no div by 5) and fizz(no div by 7)

for i in range(1,51,1):
    # print fizzbuzz if no is div by 5 and 7
    if i%5==0 and i%7==0:
        print(i , "FizzBuzz")
    # print buzz if no is divisible by 5
    elif i%5 == 0:
        print(i , "Buzz")
    # print fizz if no is div by 7
    elif i%7==0:
        print(i , "Fizz")    