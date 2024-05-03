# class Student:
#     name = "Kenil"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# Example
# class Movie:
#     Category = "Funny"
#     length = "2 hour"

# movie1 = Movie()
# print(movie1.Category)
# print(movie1.length)

# Constructor __init__()
# class Student:
#     name = "Kenil"

#     # Default constructor
#     def __init__(self):
#         pass

#     # Parameterized constructor
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database")

# s1 = Student("Kenil", 98)  # This is the self.
# print(s1.name, s1.marks)

# s2 = Student("Arhun", 45)
# print(s2.name, s2.marks)

# Class & Instance Attributes [obj attr > class attr]
# class Student: 
#     college_name = "GEC bahruch" # class Atrttribute

#     def __init__(self, name, marks):
#         self.name = name    #Object or instance attribute
#         self.marks = marks  #Object or instance attribute
#         print("adding new student in Database")

# s1 = Student("Kenil", 98)  # This is the self.
# print(s1.name, s1.marks)

# s2 = Student("Arhun", 45)
# print(s2.name, s2.marks)

# print(Student.college_name)

# Methods
# class Student: 
#     college_name = "GEC bahruch" # class Atrttribute

#     def __init__(self, name, marks):
#         self.name = name    #Object or instance attribute
#         self.marks = marks  #Object or instance attribute
    
#     def welcome(self):
#         print("Welcome", self.name)
    
#     def get_marks(self):
#         return self.marks

# s1 = Student("Kenil", 98)  # This is the self.
# s1.welcome() # call the method
# print("your marks is:",s1.get_marks())

# Static Methods:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is:", sum/3)

s1 = Student("Kenil Jagani", [99, 98, 100])
s1.get_avg() # call the method
s1.hello()

s1.name = "Bhavin Dobariya"
s1.get_avg()
