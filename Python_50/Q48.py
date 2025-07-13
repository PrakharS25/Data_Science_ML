# Demonstrate use of map(), filter(), and reduce() on a list.
from functools import reduce

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda x, y: x + y, nums)

print("Squared:", squared)
print("Even:", even)
print("Sum:", sum_all)