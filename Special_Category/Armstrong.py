# Armstrong Number:
          # The Numbers that can be represented ad the sum of the digits raised to the power of the number of digits in the number
num = int(input())
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum += digit**3
    temp //= 10
if num==sum:
    print("Armstrong")
else:
    print("Not Armstrong")

# (OR)
n = input()
sum = 0
for i in n:
    sum += int(i) + len(n)
if n==sum:
    print("Armstrong")
else:
    print("Not Armstrong")