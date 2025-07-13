# Write a Python function to find the maximum of two numbers.
def Max(a,b):
    if a > b:
        print(f"{a} is Greater than {b}")
    elif b > a:
        print(f"{b} is Greater than {a}")
    else :
        print("Both values are Same !!")

Num1 = int(input("Enter Your First Number :"))
Num2 = int(input("Enter Your Second Number :"))
Max(Num1,Num2)