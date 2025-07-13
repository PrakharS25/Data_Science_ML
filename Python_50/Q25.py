# Write a function to count uppercase and lowercase letters in a string.
def count(text):
    Up = 0
    Lo = 0
    for char in text:
        if char.isupper():
            Up += 1
        elif char.islower():
            Lo += 1
    print("Uppercase letters:", Up)
    print("Lowercase letters:", Lo)
    
Str = input("Enter a string: ")
count(Str)