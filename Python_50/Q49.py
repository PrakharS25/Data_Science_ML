# Build a small CLI app that takes user input and performs basic operations.
while True:
    print("1.Add 2.Subtract 3.Exit")
    choice = input("Enter choice: ")

    if choice == "3":
        print("Exiting Loop !!")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    else:
        print("Invalid choice")