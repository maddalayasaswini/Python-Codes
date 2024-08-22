# Sum of First N Natural numbers / Sum of N Natural Numbers:
n = int(input())
sum = 0
for i in range(1,n+1):
    sum+=i
print(sum)

#(Or)

sum1 = int((n*(n+1))/2)           #formula
print(sum1)