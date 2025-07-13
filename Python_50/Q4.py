# Write a program to count the number of vowels in a string.
Str = input("Enter The String : ")
Vow = "aeiouAEIOU"
i = 0
for a in Str :
    if a in Vow:
        i = i + 1
print(f"{Str} Has {i} Vowels !")