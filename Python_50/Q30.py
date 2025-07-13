# Create a Python program using OOP for student management (class, object, init).
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

s1 = Student("Prakhar", 37)
s1.display()