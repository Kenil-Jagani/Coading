# def num(n):
#     if (n % 2 != 0):
#         print("Weird")
    
#     if (n % 2 == 0 in range(2, 6)):
#         print("Not Weird")

#     if (n % 2 == 0 in range(6, 21)):
#         print("Weird")

#     if (n % 2 == 0 in range(21)):
#         print("Not Weird")
        
# num(3)
# --------------------------------------------------------------------------------------------------------
# def is_leap(year):
#     if (year % 4 == 0):
#         print("True")
    
#     else:
#         print("False")

# year = int(input())
# is_leap(year)

def is_leap(year):
    leap = False
    
    if (year % 4 == 0):          # if the year is normal year
        leap = True
        if year % 100 == 0:      # if the year is the century year
            if year % 400 == 0:
                leap = True
    
            else:
                leap = False
    
    return leap

year = int(input())