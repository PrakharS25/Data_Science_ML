# Accept a number and check whether it is a palindrome.
Num = input("Enter The Number to check Paimdrome :")
if (Num == Num[::-1]):
    print("It is Palindrome")
else:
    print("It is not Palindrome")