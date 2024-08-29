# Check Password 

# Write a function CheckPassword(str) which will accept the string as an 
# argument or parameter and validates the password. It will return 1 if 
# the conditions are satisfied else it’ll return 0? 

# The password is valid if it satisfies the below conditions: 
# It should contain at least 4 characters. 
# At least 1 numeric digit should be present. 
# 1 Capital letter should be there. 
# Password should not contain space or slash. 
# The starting character should not be a number.

# Sample Test Case: 
# Input: 
# bB1_89 
# Output: 
# 1

def CheckPassword(str,n):
    if n<4:
        return 0
    if str[0] == ' ':
        return 0
    cap = 0
    num = 0
    for i in range(n):
        if str[i]>='A' and str[i]<='Z':
            cap+=1
        if str[i]==' ' or str[i]=='/':
            return 0
        elif str[i].isdigit():
            num+=1
    if cap>0 and num>0:
        return 1
    else:
        return 0
str = input()
n = len(str)
print(CheckPassword(str,n))