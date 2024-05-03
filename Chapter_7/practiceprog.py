# Prob 1: create a new file "practice.txt" using python. add the following data in it:
"""
Hi everyone
we are learning File I/O
using Java.
I like programming in Java
"""

# f= open("practice.txt","w")
# f.write("Hi everyone\n""we are learning File I/O\n""using Java.\n""I like programming in Java")
# f.close()

# OR
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")


# Prob 2: WAF that replace all occurrences of "Java" with "pythone" in above file.
# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# Prob 3: Search if the word "learning" exists in the file or not.
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if (data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")

# OR
# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if (data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")

# check_for_word()

# OR
# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if (word in data):
#             print("Found")
#         else:
#             print("Not Found")

# check_for_word()

# prob 4: WAF to find in which line of the file does the word "learning" occur first.
# print-1 if word not dound. 

# def check_for_line():
#     word = "learning"
#     data = True   #starting condition in while loop
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data: # stoping condition in while loop
#             data = f.readline() # work in while loop
#             if (word in data):    #if (condition):
#                 print("Line Number=", line_no) # statement in if
#                 return
#             line_no += 1 
    
#     return -1

# print(check_for_line()) # call the function

# Prob 5: From a file containing numbers separated by comma, print the count of even numbers.
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]

# use of split method
count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1

print(count)
