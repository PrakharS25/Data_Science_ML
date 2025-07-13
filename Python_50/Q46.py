# Create a simple login system using dictionary and input.
users = {"admin": "1234", "user": "pass"}

username = input("Username: ")
password = input("Password: ")

if users.get(username) == password:
    print("Login successful")
else:
    print("Invalid credentials")