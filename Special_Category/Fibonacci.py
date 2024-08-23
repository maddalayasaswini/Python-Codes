# Fibonacci Series upto nth term:
num = int(input())
a,b = 0,1
print(a, b, end = ' ')
for i in range(2,num):
    c = a+b
    a = b
    b = c
    print(c, end = ' ')