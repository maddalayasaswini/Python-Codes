# Friendly pair or amicable pair:
          # The numbers whose ( sum of divisors ) / number ratio is same.
num1 = int(input())
num2 = int(input())
sum1 = 0
for i in range(1, num1):
    if num1 % i == 0:
        sum1 += i
sum2 = 0
for j in range(1, num2):
    if num2 % j == 0:
        sum2 += j
if sum1%num1==0 and sum2%num2==0 :
    print("Friendly pair")
else:
    print("Not a Friendly pair")