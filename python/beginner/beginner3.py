#Write a program that takes in an integer from the user and outputs whether it is even or odd.
#Output must be in format: "{number} is even" or "{number} is odd"
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
