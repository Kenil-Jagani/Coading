#Prob 1: WAP to check if a number entered by the user is odd or even
# num=int(input("Enter the number="))

# if (num % 2 == 0):
#     print(num,":This Number is Even")
# else:
#     print(num, ":This Number is odd")

#Prob 2: WAP to find the greatest of 3 number entered by the user.
# a=int(input("Enter first number ="))
# b=int(input("Enter second number ="))
# c=int(input("Enter third number ="))

# if(a>=b and a>=c):
#     print("Gratest number is",a)
# elif(b>=c):
#     print("Gratest number is",b)
# else:
#     print("Gratest number is",c)

#Prob 3: WAP to check if a number is a multiple of 7 or not.
# num = int(input("Enter the number="))

# if (num % 7 == 0):
#     print("Multiple of 7.")
# else:
#     print("Not multiple of 7.")

#Prob 4: WAP to find the greatest of 4 number entered by the user.
a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
c= int(input("Enter the third number:"))
d= int(input("Enter the foth number:"))

if (a>=b and a>=c and a>=d):
    print("Gratest number is", a)

elif (b>=c and b>=d):
    print("Gratest number is", b)

elif (c>=d):
    print("Gratest number is", c)

else:
    print("Gratest number is", d)


