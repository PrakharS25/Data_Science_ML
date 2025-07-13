# Write a program to implement a simple calculator using functions.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"

def calculator():
    print("Welcome To Basic Calculator !!!!!")
    a = int(input("Enter the Value of A: "))
    b = int(input("Enter the Value of B: "))

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    opt = int(input("Enter Your Choice: "))

    if opt == 1:
        result = add(a, b)
        print(f"The Addition of {a} and {b} is: {result}")
    elif opt == 2:
        result = subtract(a, b)
        print(f"The Subtraction of {a} and {b} is: {result}")
    elif opt == 3:
        result = multiply(a, b)
        print(f"The Multiplication of {a} and {b} is: {result}")
    elif opt == 4:
        result = divide(a, b)
        print(f"The Division of {a} and {b} is: {result}")
    else:
        print("Invalid Operator")

    print("Thank You !!")

calculator()