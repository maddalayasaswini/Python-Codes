# Prime Factors of a Number:
num = int(input())
prime_factors = []
for i in range(2,num+1):
    if num%i == 0:
        prime_factors.append(i)
        num//=i
print(prime_factors)