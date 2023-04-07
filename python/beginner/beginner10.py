#Write a program that takes in a string from the user and outputs whether the string is a palindrome (meaning it reads the same forwards and backwards).

string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
