#Set in python is mutable but each elements in the set must be unique & immutable.
# immutable : str, int, float, boolean, Tuple, elements in set
# mutable: list, dictionary, set 

# nums = {1, 2.3, 3, "Kenil", "Jagani"} 
# print(nums)
# print(type(nums))
# print(len(nums))

# set1 = set() ---> Empty set

# Set Methods
# (1) set.add(el)
# set1 = set()
# set1.add(1)
# set1.add((2,3,4))
# set1.add("Kenil")

# print(set1)

# (2) set.remove(el)
# set2 = {1, 2, 3, 4}
# set2.remove(4)
# print(set2)

# (3) set.clear()
# set3 = {1, 2, 3, 4}
# set3.clear()
# print(len(set3))

# (4) set.pop()
# set4 = {1, 3.5,"Kenil", 2, 4}
# print(set4.pop())

# (5) set.union(set2)
# set5 = {1,2,3}
# set6 = {3,4,5}
# print(set5.union(set6))

# (6) set.intersection(set2)
set5 = {1,2,3}
set6 = {3,4,5}
print(set5.intersection(set6))