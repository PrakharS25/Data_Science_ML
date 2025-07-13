# Write a Python program to find the largest of three numbers.

Num1 = int(input("Enter Number 1 : "))
Num2 = int(input("Enter Number 2 : "))
Num3 = int(input("Enter Number 3 : "))

if Num1 > Num2 and Num1 > Num3:
    print(f"{Num1} is The Largest !")
elif Num2 > Num1 and Num2 > Num3:
    print(f"{Num2} is The Largest !")
elif Num3 > Num1 and Num3 > Num2:
    print(f"{Num3} is The Largest !")
else :
    print("Invalid Integers To check The Largest Number !")