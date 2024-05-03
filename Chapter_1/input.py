#Taking input from user & printing it
name = input("name : ")
age = int(input("age: "))
Price= float(input("price: "))

print("My name is", name, "and I am", age, "years old.")

#input always give string type output, input converts int into str.
#that's why we use Type casting such as int(input("age: "))

val1=input("ENTER VALUE: ")
print(type(val1), val1)

val2=int(input("ENTER VALUE: "))
print(type(val2), val2)

val2=float(input("ENTER VALUE: "))
print(type(val2), val2)