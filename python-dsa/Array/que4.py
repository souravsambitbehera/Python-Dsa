# Question 4:
# Write a Python program to count the frequency of each element in a list. The program should return a dictionary where the keys are the elements, and the values are the counts of those elements in the list.


nums = [1,2,1,2,3,2]
occr_num = {}
for item in nums:
    if item in occr_num.keys():
        occr_num[item] +=1
    else:
        occr_num[item] = 1

print(occr_num)