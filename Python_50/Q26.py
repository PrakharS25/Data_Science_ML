# Write a Python program using a lambda function to square all elements in a list.
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)