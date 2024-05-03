# del keyword  -------------------------------------------------------------
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student ("Kenil")

# del s1
# print(s1)
 
# Private (like) attributes & methods  ---------------------------------------
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("12345","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())

# Example:

# class Person:
#     __name= "anonymous" #Private Attribute 

#     def __hello(self):  #private method
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.welcome())

# Inheritance ------------------------------------------------------------
# Single Inheritance
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar ("Fortuner")
# car2 = ToyotaCar ("Prius")

# print(car1.start())

# Multi-level Inheritance  -------------------------------------------------
# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__ (self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()

# Multipal Inheritance -----------------------------------------------------
# class A:
#     varA = "welcome to class A"

# class B: 
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# Super Method -------------------------------------------------------------

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)  # call to parent class method    
#         self.name = name
#         super().start()   # call to parent class method

# car1 = ToyotaCar("prius", "Electric")
# print(car1.type)

# Class decorator ------------------------------------------------------------
# class Person:
#     name = "anonymous"

#     # def changeName(self, name):
#     #     # Person.name = name
#     #     self.__class__.name = "Rahul kumar"

#     @classmethod    #decorator 
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Rahul kumar")
# print(p1.name)
# print(Person.name)

# Property decorator ----------------------------------------------------------
# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
#         self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

#     def calpercentage(self):
#         self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.phy)
# stu1.calpercentage()
# print(stu1.percentage)

# OR
# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.maths)/3) + "%"

# stu1 = Student (98, 97, 100)
# print(stu1.percentage)

# stu1.phy = 89
# print(stu1.percentage)


# Dunder function  ---------------------------------------------------------------
# Example of complex number
# This is without dunder function
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img,"j")

#     def add(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img 
#         return Complex(newReal, newImg)

# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(5, 8)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

# same code with dunder fuction

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img 
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(5, 8)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()