# Abundant number:
           # A Number that is smaller than the sum of all it's factors except the number itself 
num = int(input())
sum = 1
for i in range(2,num):
    if num%i==0:
        sum = sum+i
if (sum>num):
    print("Abundant number")
else:
    print("Not an Abundant number")