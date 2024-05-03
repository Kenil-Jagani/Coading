#Lists are mutable.
#List with Index
# marks=[94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])

#In list we can access and change the values but in string we only can eccess not change.

# student=["Kenil", 95, "Surat"]
# print(student[0])
# student[0] = "Jagani"
# print(student)

#List slicing
# marks=[94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks[1:4])
# print(marks[-3:-1])

#List Methods
#(1) list.append()  [add to the list]
# list=[2,1,3]
# list.append(4)
# print(list)

#(2) list.short()    [arrange in Assending order]
# list = [2,1,3]
# print(list.append(4))
# print(list.sort())
# print(list)

#(3) list.short(revers=True)   [Arrange in Decending order]
# list = [2,1,3]
# print(list.append(4))
# print(list.sort(reverse = True))
# print(list)

# list = ["Mango","Banana","Orange"]
# print(list.sort(reverse = True))
# print(list)

#(4) list.reverse()
# list = ["Mango","Banana","Orange"]
# list.reverse()
# print(list)

#(5) list.insert(idx,el)
# list=[2,1,3]
# list.insert(1,5)
# print(list)

#(6) list.remove()   [Remove first occurance of element]
# list=[2,1,3,1]
# list.remove(1)
# print(list)

#(7) list.pop(idx)  [remove perticular value at particular index]
list=[2,1,3,1]
list.pop(2)
print(list)