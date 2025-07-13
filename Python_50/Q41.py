# Implement a program to demonstrate try-except-finally for exception handling.
try:
    x = int(input("Enter a number: "))
    print(100 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This runs no matter what.")