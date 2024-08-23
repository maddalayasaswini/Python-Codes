# Strong Number:
             # A Number that is equal to the sum of the factorial of it's individual digits.
num = int(input())
sum = 0
temp = num
while temp > 0 :
    digit = temp% 10
    fact = 1
    for i in range(1, digit+1):
        fact*=i
    sum+=fact
    temp //= 10
if num==sum:
    print("Strong Number")
else:
    print("Not a Strong Number")