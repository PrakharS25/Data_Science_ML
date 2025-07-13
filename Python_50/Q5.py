# Create a calculator using if-else (add, subtract, multiply, divide).
a = int(input("Enter the Value of A :"))
b = int(input("Enter the Value of B :"))

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exit the Loop")

while(True):
    Opt = int(input("Enter Your Choice :"))
    if Opt == 1:
        print(f"The Addition of {a} and {b} is :",a+b)
    elif Opt == 2:
        print(f"The Subtraction of {a} and {b} is :",a-b)
    elif Opt == 3:
        print(f"The Multiplication of {a} and {b} is :",a*b)
    elif Opt == 4:
        print(f"The Division of {a} and {b} is :",a/b)
    elif Opt == 5:
        print("Exiting The Loop !!")
        break
    else:
        print("Invalid Operator")
    print("Thank You !!")