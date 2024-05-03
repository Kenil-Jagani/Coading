# Prob 1: Store following word meanings in a python dictionary:
# table : "a piece of funrniture","list of facts & figures"
# cat : "a small animal"

# dict = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"]
# }

# print(dict)

# prob 2: You are given a list of subjects for students. Assum one classroom is required for 1 subject. How many classrooms are need by all students.
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"

# subject_set = {"python", "java", "C++", "python", "javascript","java", "python", "java", "C++", "C"}

# print("Total Number of Classroom needed :",len(subject_set))
# print("Subjects: ",subject_set)

# prob 3: WAP to enter marks of 3 sujects from the user and store them in a dictionary.
# Start with an empty dictonary & add one by one. Use subject name as key & marks as value.

# marks = {}

# x = int(input("Enter phy: "))
# marks.update({"phy" : x})

# x = int(input("Enter chem: "))
# marks.update({"chem" : x})

# x = int(input("Enter math: "))
# marks.update({"math" : x})

# print(marks)

# prob 4: FIgure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)


# way 1:
# set=set()
# set.add(9)
# set.add("9.0")
# way 2:
set={
    ("float", 9.0),
    ("int", 9)
}

print(set)

