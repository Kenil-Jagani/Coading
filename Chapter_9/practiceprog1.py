# Prob 1: Define a Circle class to create with radius r using the constructor.
# Define an Area() method of the class which calculate the area of the circle.
# Define a perimeter() method of the class which allows you to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self, r):
#         self.r = r

#     def Area(self):
#         return (22/7) * self.r ** 2

#     def Perimeter(self):
#         return 2 * (22/7) * self.r

# c1 = Circle(21)
# print(c1.Area())
# print(c1.Perimeter())

# Prob 2: Define Employee class with attributes role, department & salary. This class also a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role =", self.role)
#         print("Department =", self.dept)
#         print("Salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")

# engg1 = Engineer ("Elon Musk", "40")
# engg1.showDetails()

# Prob 3: Create a class called Order which stores item & its price.
# Use Dunder fuction __gt__() to convey that:
# order1 > order2 if price of order1>price of order2. 

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("Tea", 15)

print(odr1 > odr2)