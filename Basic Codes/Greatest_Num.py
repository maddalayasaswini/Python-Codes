# Greatest of 2 or 3 Numbers:
a,b,c = map(int,input().split())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

# (Or)

print(max(a,b,c))          #max() is a bulit-in function to find maximum number