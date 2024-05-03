#if-elif-else (SYNTAX)
# age = int(input("Enter your Age:"))
# if(age>= 18):
#     print("You can vote & apply for licence") 

# elif(age<18):
#     print("You can not vote & can not apply for licence")

# else:
#     print("You can not vote & can not apply for licence")
 
#And
# age = int(input("Enter your Age:"))
# if(age == 18):
#     print("You can vote & apply for licence") 

# if(age >= 18):
#     print("You can not vote & can not apply for licence")

#Another Example
# light = "Pink"

# if (light == 'Red'):
#     print("stop")
# elif(light == "Green"):
#     print("Go")
# elif(light == "Yellow"):
#     print("look")
# else:
#     print("light is broken")

#Another Example: Grade students based on marks
""" marks >=90, grad = "A"
90>marks >= 80, grad="B"
80>marks >= 70, grad="C"
70>marks, grad="D"
"""
# marks=int(input("Enter your marks:"))

# if(marks>=90):
#     print("You securing grade = A")
# elif(marks>=80 and marks<90):
#     print("You securing grade = B")
# elif(marks>=70 and marks<80):
#     print("You securing grade = C")
# elif(marks<70):
#     print("You securing grade = D")

#OR
# marks=int(input("Enter your marks:"))

# if(marks>=90):
#     grade = "A"
# elif(marks>=80 and marks<90):
#     grade = "B"
# elif(marks>=70 and marks<80):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of the student =", grade)

#Nesting
age = 18

if(age >= 18):
    if (age >= 80):
        print("Cannot Drive")
    else:
        print("Can Drive")

else:
    print("Cannot Drive")
