#prob 1: WAP to ask the user to enter names of their 3 favorite movie & store then in a list.

# name=[]
# name1= str(input("First Movie Name:"))
# name2= str(input("Second Movie Name:"))
# name3= str(input("Third Movie Name:"))

# name.append(name1)
# name.append(name2)
# name.append(name3)

# print(name) 

#OR
# name=[]
# name.append(input("First Movie Name:"))
# name.append(input("Second Movie Name:"))
# name.append(input("Third Movie Name:"))

# print(name) 

#Prob 2: WAP to check if a list contains a palindrome of elements. (Hint: use copy()method) [1,2,3,2,1] [1,"abc","abc",1]
# list1= [1,2,1]
# list2= [1,2,3]

# copy_list1= list1.copy()
# copy_list1.reverse()

# if (copy_list1 == list1):
#     print("Palindrome")

# else:
#     print("Not palindrome")

#prob 3: WAP to count the number of students with the "A" grade in the following tuple. ["c","D","A","A","B","B","A"]
# grade= ("c","D","A","A","B","B","A")

# print(grade.count("A"))

#prob 4: Store the above values in a list & sort them from "A" to "D".
grade=["A", "B", "C", "D"]
grade.sort()
print(grade)
