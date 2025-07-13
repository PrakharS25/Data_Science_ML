# Accept a list of numbers and return the average.
List = []
Dig = int(input("Enter The Number of elements :"))
for i in range(Dig):
    A = int(input(f"Enter the {i+1} element of List :"))
    List.append(A)
# print(List)
print("Average of The List is :",sum(List)/Dig)