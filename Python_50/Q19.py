# Accept a list and sort it without using sort() function.
List = []
Dig = int(input("Enter The Number of elements :"))
for i in range(Dig):
    A = int(input(f"Enter the {i+1} element of List :"))
    List.append(A)
for i in range(len(List)):
    min_index = i
    for j in range(i + 1, len(List)):
        if List[j] < List[min_index]:
            min_index = j
    List[i], List[min_index] = List[min_index], List[i]
print("Sorted list:", List)