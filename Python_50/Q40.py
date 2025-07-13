# Write a function to find common elements between two lists.
def common(l1, l2):
    return list(set(l1) & set(l2))
print(common([1, 2, 3], [2, 3, 4]))