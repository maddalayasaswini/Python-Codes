# Perfect Square:
num = int(input())
is_perfect_square = False
for i in range(1,num):
    if  i*i == num:
        is_perfect_square = True
        break
if is_perfect_square:
    print("Perfect Square")
else:
    print("Not A Perfect Square")