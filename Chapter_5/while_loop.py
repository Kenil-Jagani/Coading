# Loop : Types (1) while & (2) For

# i = 1 #Iterator  & process calle Iteration
# while i <= 5 :
#     print("Hello", i)
#     i += 1

# print(i)

# i=10 
# while i >=1 :
#     print(i)
#     i -= 1

# Important key words
# (1) Break
# i =1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i += 1

# (2) Continue
# i=0
# while i<=5:
#     if (i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

#Example: we we print only odd numbers from 1 to 10.
# i = 1
# while i <= 10:
#     if (i%2 == 0):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

#Example: we we print only even numbers from 1 to 10.
i = 1
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue #skip
    print(i)
    i += 1