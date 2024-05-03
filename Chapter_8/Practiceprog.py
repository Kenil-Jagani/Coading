# Prob 1: Creat student class that takes name & marks of 3 subjects as arguments in constructor.
# then creat a method to print the average.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is:", sum/3)

# s1 = Student("Kenil Jagani", [99, 98, 100])
# s1.get_avg() # call the method

# s1.name = "Bhavin Dobariya"
# s1.get_avg()

# Prob 2: Create account class with 2 attributes - balance & account no.
# create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal 
        self.account_no = acc
    
    #Debit method
    def debit (self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited.")
        print("Total balance =", self.get_balance())

    #credit method
    def credit (self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000000, 123456789234)
acc1.debit(10000)
acc1.credit(5000)
