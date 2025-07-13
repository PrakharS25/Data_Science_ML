# Find the second largest number in a list.
List = []
Dig = int(input("Enter The Number of elements :"))
for i in range(Dig):
    A = int(input(f"Enter the {i+1} element of List :"))
    List.append(A)
List.remove(max(List))
print("The second largest number in a list is :",max(List))