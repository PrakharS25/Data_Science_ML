# Find the sum of digits of a number using a while loop.
Num = int(input("Enter the Number :"))
Q = Num
Sum = 0
while Num > 0 :
    A = Num % 10
    Sum = A + Sum
    Num = Num // 10
print(f"Sum of {Q} is : {Sum}")