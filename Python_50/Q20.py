# Write a function that checks if a string is a pangram.
def Pang(sentence):
    sentence = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True
text = input("Enter a sentence: ")
if Pang(text):
    print("It is a pangram.")
else:
    print("It is not a pangram.")
