# Write a program to print the Fibonacci series up to n terms.
Num = int(input("Enter number of terms : "))
a = 0
b = 1
for i in range(Num):
    print(a, end="")
    a, b = b, a + b