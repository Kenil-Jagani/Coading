#Dictionary: mutable, unordered, do not repet same key another time.
# info={
#     "key" : "value",
#     "name" : "Kenil",
#     "age" : 20.7,
#     "is_adult" : True,
#     "marks" : [69, 65, 49],
#     "Topics" : ("dict","set"),
#     66.5 : 678   
# }
# print(info)
# print(type(info))

#use insted of Index.
# print(info["name"])

#mutable [new value assign & new Key : value addition]
# info["name"] = "Kenil_Jagani"
# info["surname"] = "Jagani"
# print(info)

#Empty Dictionary
# null_dict = {}  
# null_dict["Name"] = "ApnaCollege"
# print(null_dict)

#Nested Dictionary
# student={
#     "name" : "Kenil_Jagani",
#     "Subjects" : {
#         "chem" : 99,
#         "phy" : 100,
#         "Maths" : 100
#     }
# }
# print(student)
# print(student["Subjects"])
# print(student["Subjects"]["chem"]) 

#Dictionary Methods
#(1) myDict.keys()
student={
    "name" : "Kenil_Jagani",
    "Subjects" : {
        "chem" : 99,
        "phy" : 100,
        "Maths" : 100
    }
}
# print(student.keys())

# Type casting:
# print(list(student.keys()))

#(2) myDict.values()
# print(list(student.values()))

#(3) myDict.items()
# print(list(student.items()))

# we can individualy excess tuples
# pairs = list(student.items())
# print(pairs[0]) 

#(4) myDict.det("key")
# print(student.get("Subjects"))
# OR
# print(student["Subjects"])

# differance:
# print(student["name2"])  ---> in output get Error
# print(student.get("name2")) ---> in output get None 

#(5) myDict.update(new Dict) OR ({Pair})
# student.update({"city" : "Surat", "age" : 20})
student.update({"name" : "JK", "age" : 20})
print(student)