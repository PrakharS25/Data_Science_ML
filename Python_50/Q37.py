# Create a function that takes a list and returns only unique elements.
def unique_list(lst):
    return list(set(lst))
print(unique_list([1, 2, 2, 3, 4, 4]))