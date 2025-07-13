# Write a program to check if a number is prime.
Num = int(input("Enter Your Number: "))
if Num > 1:
    for i in range(2, Num):
        if Num % i == 0:
            print(f"{Num} is Not Prime")
            break
    else:
        print(f"{Num} is Prime")
else:
    print(f"{Num} is Not Prime")