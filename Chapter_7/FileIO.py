
# f = open("D:\PERSONAL\Data Science\Apana College\Python\Chapter_7\demo.txt", "rt")

# data = f.read(5)
# print(data)

# f.close()

# f.Readline()
# f = open("D:\PERSONAL\Data Science\Apana College\Python\Chapter_7\demo.txt", "rt")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

# Write mode
# f = open("D:\PERSONAL\Data Science\Apana College\Python\Chapter_7\demo.txt", "w")
# f.write("NO I am not Kenil Jagani.\nI am student of life.")

# f.close()

# Append mode
# f = open("demo.txt", "a")
# f.write("Hyy, I am Kenil Jagani.")

# f.close()

# open file which not exist
# f = open("sample.txt", "w")
# f.close()

# OR
# f = open("sample.txt", "w")
# f.close()

# r+ mode
# f =open("demo.txt", "r+")  #Overwrite at the starting of the file.
# f.write("ABC")
# print(f.read())
# f.close()

# w+ mode
# f =open("demo.txt", "w+")  #Truncate(overwrite) whole file.
# print(f.read())
# f.write("oyy, where are you going.")
# f.close()

# a+ mode
# f =open("demo.txt", "a+")  #stream is positioned at the end of file.
# print(f.read())
# f.write("\nI am going to the train.")
# f.close()

# With syntax
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("New Data.")

# Deleting file [os module]
import os
os.remove("sample.txt")