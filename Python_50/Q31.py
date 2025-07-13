# Write a program to read a file and count the number of lines and words.
with open(r"C:\Users\prakh\Downloads\my code\Python\DS And Ml\Assignments\Python_50\sample.txt", "r") as file:
    lines = file.readlines()
    words = sum(len(line.split()) for line in lines)

print("Lines:", len(lines))
print("Words:", words)