#Write a program that takes in a list of strings from the user and outputs the shortest string in the list.
string_list = input("Enter a list of strings, separated by spaces: ").split()
shortest = min(string_list, key=len)
print("The shortest string is:", shortest)
