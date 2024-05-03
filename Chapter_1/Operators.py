#Arithmetic Opeartor
a=5
b=8

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b) #Riminder
print(a**b)

#Relational or comparision Operators
print(a==b)  #False
print(a!=b)  #True
print(a>b)  #False
print(a<b)  #True
print(a>=b)  #False
print(a<=b)  #True

#Assignment Operators
num=10
num +=10  #same for -=, *=, /=, //=, %=, **=

print(num)

#Logical Operators
print(not True) #False
print(not False) #True
print(not (a<b)) #False

"""
When val1 and val2 both are True then and then (and) operator gives us True
If One of the val1 and val2 is False then (and) operator gives False
"""
val1= True
val2= False

print("AND operator: ", val1 and val2)
print("OR operator: ", val1 or val2)
print("OR operator: ", a==b or a!=b)
print("OR operator: ", a==b or a>=b)

# and and or operator works with two values when not operator work with one value