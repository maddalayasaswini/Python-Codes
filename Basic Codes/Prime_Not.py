# Prime number or not:
num = int(input())
for i in range(1, num+1):
    if num%i ==0 :
        print("Not a Prime Number")
        break
    else:
        print("Prime Number")