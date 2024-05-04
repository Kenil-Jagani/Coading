# Guess the number -----------------------------------------------------------------------------------------------------
# import random   #Random Module

# target = random.randint(1, 100)

# while True:
#     userChoice = input("Guess the number or Quit: ")
    
#     if(userChoice == "Quit"):
#         break

#     userChoice = int(userChoice)
#     if (userChoice == target):
#         print("Success: Correct Guess!!")
#         break
#     elif(userChoice < target):
#         print("Yoyr number was too small. take a bigger guess...")
#     else:
#         print("Yoyr number was too big. take a smaller guess...")

# print("----- Game Over -----")

# Random Password Generator --------------------------------------------------------------------------------------------
# import random  # Random Module
# import string  # String Module

# password_len = 12
# charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(password_len):
#     password += random.choice(charValues)

# print("Your random password is:", password)

# using same code with list comprihantion [function for i in range(n)]
import random  
import string  

password_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charValues) for i in range(password_len)])

print("Your random password is:", password)

# ----------------------------------------------------------------------------------------------------
