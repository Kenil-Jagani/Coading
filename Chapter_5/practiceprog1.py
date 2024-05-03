# prob 1: print numbers from 1 to 100.
# i = 1
# while i<=100:
#     print(i)
#     i += 1

# prob 2: print numbers from 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i -= 1

# prob 3: print the multiplication table of a number n.
# i= 1 
# j = int(input("table number: "))

# while i<=10:
#     print(j, "*", i, "=", j*i)
#     i += 1

# prob 4: Print the element of the following list using loop.
# [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])  #nums[0], nums[1], nums[2], ....
#     idx += 1
# another eample
# Heroes= ["ironman", "Thor", "Superman", "Batman"]
# idx=0
# while idx < len(Heroes):
#     print(Heroes[idx])
#     idx += 1

# prob 5: Search for a number x in this tuple using loop.
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter number from Tuple given:" ))
i=0 #initialization
while i<len(nums):
    if (nums[i] == x):
        print("FOUND at idx:", i)
        break
    else:
        print("finging...")
    i += 1
print("End of loop")
