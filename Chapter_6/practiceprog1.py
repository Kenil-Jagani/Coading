# Peob 1: WAF to print the length of a list. (list is the parameter)
# def print_len(a):
#     print(len(a))

# print_len([1, 2, 3, 4, 5])

# Prob 2: WAF to print the elements of a list in a single line (list is the parameter)
# list = ["movie", "song", "Dance"]
# num = [1, 2, 3, 4, 5]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(list)

# Prob 3: WAF to find the factorial of n.(n is the parameter)
# def fect_n(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
#     return fact # return if we want
    
# fect_n(5)

# Prob 4: WAF to convert USD to INR.
# def converter(usd_val):
#     inr_val = usd_val*83.49
#     print(usd_val,"USD =", inr_val, "INR")
#     return inr_val # return if we want

# converter(3)

# Prob 5: WAP in which input is number and if it is odd then in return it give a string "ODD" anf if number is even then it will give "EVEN"
def num(n):
    if (n%2 != 0):
        print(n, "is ODD number.")
    else:
        print(n, "is EVEN number.")

num(2)