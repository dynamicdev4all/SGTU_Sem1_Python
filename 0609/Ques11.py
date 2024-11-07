# User Input :
# a.	Person Name
# b.	Person gender
# c.	Person Age
# d.	Person city (Metro or Non-Metro)

name = input("Enter ur name :")
age = int(input("Enter ur age :"))
gender = input("Enter ur gender (M or F):")
city = input("Enter ur city (M or N) :")
# if person age is 25 to 35 and gender is male and city is metro , Output is Premium is 6%

if(age>= 25 and age<=35 and gender=="M" and city == "M"):
    print("Premium is 6%")

# if person age is 25 to 40 and gender is male and city is non-metro, Output is Premium 4%
elif(age>=25 and age<=40 and gender=="M" and city == "N"):
    print("Premium is 4%")

# if person age is 25 to 42 and gender is female and city is Metro, Output is Premium 3%
elif(age>=25 and age<=42 and gender=="F" and city == "M"):
    print("Premium is 3%")

# if person age is 25 to 45 and gender is female and city is non-metro , output is Premium 2%
elif(age>=25 and age<=45 and gender=="F" and city == "N"):
    print("Premium is 2%")