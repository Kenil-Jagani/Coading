# prob 1: Write a recursive function to calculate the sum of first natural numbers.
# def natural(n):
#     if(n == 0):
#         return 0
#     return natural(n-1) + n

# print(natural(5))

# prob 2: Write a recursive function to print all element in a list. Hint: use list & index as parameter.
# def print_list(list, idx=0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["Mango", "Litchi", "Apple", "Banana"]

# print_list(fruits)

# OR
def print_list(list, idx):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["Mango", "Litchi", "Apple", "Banana"]

print_list(fruits, 0)

