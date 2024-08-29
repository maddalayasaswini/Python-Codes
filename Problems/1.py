# Small Large Sum 

# Write a function SmallLargeSum(array) which accepts the array as an argument or 
# parameter, that performs the addition of the second largest element from the 
# even location with the second largest element from an odd location? 

#  Rules: 
# All the array elements are unique. 
# If the length of the array is 3 or less than 3, then return 0. 
# If Array is empty then return zero. 

# Sample Test Case 1: 
# Input: 
# 6 
# 3 2 1 7 5 4 
# Output: 
# 7 

# Explanation: The second largest element in the even locations (3, 1, 5) is 3. The 
# second largest element in the odd locations (2, 7, 4) is 4. So the addition of 3 and 
# 4 is 7. So the answer is 7. 

# Sample Test Case 2: 
# Input: 
# 7 
# 4 0 7 9 6 4 2 
# Output: 
# 10

lenght = int(input())
array = list(map(int, input().split()))
even_arr = []
odd_arr = []
for i in range(lenght):
    if i%2==0:
        even_arr.append(array[i])
    else:
        odd_arr.append(array[i])
even_arr = sorted(even_arr)
odd_arr = sorted(odd_arr)
print(even_arr[-2]+odd_arr[-2])