# Sum of Numbers in given Range:
a = int(input())
b = int(input())
sum = 0
for i in range(a,b+1):
    sum += i
print(sum)

#(Or)

sum1 = int((b*(b+1)/2) - (a*(a+1)/2) + a)  #formula
print(sum1)