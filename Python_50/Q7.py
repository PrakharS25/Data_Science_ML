# Display the multiplication table of a given number.
Num = int(input("Enter A Number :"))
i=1
for i in range(1,11):
    b = Num * i
    print(f"{Num} X {i} = {b}")
    i=i+1