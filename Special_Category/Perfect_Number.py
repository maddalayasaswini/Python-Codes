# Perfect Number:
          # A Number that can be represented as the sum of all the factors of the number.
num= int(input())
sum = 0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")