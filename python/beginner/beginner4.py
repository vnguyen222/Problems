#Write a program that takes in a list of numbers from the user and outputs the largest number in the list.
#Output should be in format: "The largest number is {number}"

num_list = input("Enter a list of numbers, separated by spaces: ").split()
num_list = [int(num) for num in num_list]
largest = max(num_list)
print("The largest number is", largest)
