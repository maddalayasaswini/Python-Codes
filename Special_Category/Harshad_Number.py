# Harshad Number:
          # A Number that is divisible by the sum of it's digits.
num = int(input())
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10
if num % sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")