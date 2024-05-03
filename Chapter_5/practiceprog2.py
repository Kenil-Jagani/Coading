# Prob 1: print the element of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for el in list:
#     print(el)

# prob 2: search for a number x in this tuple using loop: [called linear search]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 9

# idx =0
# for el in tup:
#     if (el == x):
#         print("Number is found at idx", idx)
#     idx += 1

# solve probs below using for & range():
# prob 3: print numbers from 1 to 100

# for el in range(1, 101):
#     print(el)

# prob 4: Print numbers from 100 to 1

# for i in range(100,0,-1):
#     print(i)

# prob 5: Print the multiplication table of number n
n=int(input("Enter the Table number you want: "))
for i in range(1,11):
    print(n, "*", i, "=", n*i)

