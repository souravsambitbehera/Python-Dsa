# Question 5:
# Write a Python program that takes a list of numbers and returns a new list with all the even numbers from the original list.
def getList(arr):
    even_list = []
    for item in arr:
        if item % 2 == 0:
            even_list.append(item)
    return even_list
arr = [1, 2, 3, 4, 5, 6, 7, 8]
value = getList(arr)  
print(value)

# def getList(arr):
#     return [item for item in arr if item % 2 == 0]