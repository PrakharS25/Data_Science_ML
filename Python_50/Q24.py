# Accept a list and print all elements greater than 50.
List = []
Above = []
Dig = int(input("Enter The Number of elements :"))
for i in range(Dig):
    A = int(input(f"Enter the {i+1} element of List :"))
    List.append(A)
for i in range(Dig):
    if List[i] > 50:
        Above.append(List[i])
print("Elements Greater than 50 are :",Above)