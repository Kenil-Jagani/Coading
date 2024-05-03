#in list we use [] and in Tuples we use ().
#Tuples are immutable.

# tup=() #Empty typle
# tup=(1,) #Single value tuple

# tup=(2,1,3,1)
# print(type(tup))

#index
# print(tup[0])

#Slicing of Tuple
# tup = (1,2,3,4)
# print(tup[1:3])

# Methods in Tuple
#(1) tup.index(el)  [index of first occurance]
tup = (1,2,3,2)
print(tup.index(2))

#(2) tup.count(el)
# tup = (1,2,3,1)
# tup = tup.count(1)
# print(tup)