# Automorphic number:
             # A number whose square ends with the same number
num = int(input())
a = str(num)
num2 = pow(num,2)
b = str(num2)

if b.endswith(a):
    print("Automorphic Number")
else:
    print("Not a Automorphic Number")