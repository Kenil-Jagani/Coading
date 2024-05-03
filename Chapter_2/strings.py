#Escape Sequence Characters
# str1="My Name is Kenil.\nI am 20 years old."
# print(str1)
# print (len(str1))
# str1="My Name is Kenil.\tI am 20 years old."
# print(str1)

#Basic Operations on String
#Concatenation
# name1="Kenil"
# len1= len(name1)

# name2="Jagani"
# len2= len(name2)

# final_str= name1 + " " +name2
# print(final_str)
# print(len(final_str))

# print(name1+name2)

#Index
# word1= "Kenil"
# ch = word1[3]
# print(ch)

#Slicing
# str= "Kenil Jagani"
# print(str[6:12])
# #OR
# print(str[6:len(str)])
# #OR
# print(str[:12])
# #OR
# print(str[6:])

# #Negative Index
# word="Apple"
# print(word[0:-3])

#String Functions
#(1) str.endswith("_")
# str1 = "My name is String."
# print(str1.endswith("ing."))
# print(str1.endswith("ig."))

#(2) str.capitalize()
# str2 = "my name is String."
# print(str2.capitalize())
# #OR
# str2 = str2.capitalize()
# print(str2)

#(3) str.replace(old,new)
# str3 = "My name is String."
# str3= str3.replace("String","Kenil") 
# print(str3)

#(4) str.find("word")
# str4 = "My name is String."
# str4 = str4.find("n") 
# print(str4)

#(5) str.count("word")
str5 = "My name is name." 
print(str5.count("name"))