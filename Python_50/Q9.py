# Write a program to find the factorial of a number using a loop.
Num = int(input("Enter The Number :"))
a = Num
if Num == 0:
    print("Factorial of 0 is : 0")
else :
    for i in range (1,Num):
        Num = Num*i

print(f"Factorial of {a} is : {Num}")