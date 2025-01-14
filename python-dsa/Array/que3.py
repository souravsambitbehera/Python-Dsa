# Question 3:
# Write a Python program to find the largest number in a list of integers without using the built-in max() function.



nums = [2,5,7,9,2,1]
largest_num = nums[0]
for item in nums:
    if largest_num < item:
        largest_num = item
print(largest_num)