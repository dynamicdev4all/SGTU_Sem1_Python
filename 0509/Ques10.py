# 10.	Find out the grade , according to given percentage of the user.
# d.	<50 print ‘D’ Grade
# c.	>=50 print ‘C’ Grade
# b.	>=70 print ‘B’ Grade
# a.	>=90 print ‘A’ Grade


p_marks = float(input("Enter physics marks"))
c_marks = float(input("Enter chemistry marks"))
m_marks = float(input("Enter maths marks"))

per = ((p_marks + m_marks + c_marks)/300) *100

if (per < 50):
    print("D grade")
elif (per >=50):
    print("C grade") 
elif (per > 70):
    print("B grade")
elif (per > 90):
    print(" A grade") 


# We have to read about the operators first  