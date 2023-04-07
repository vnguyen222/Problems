#Write a program that takes in a list of integers from the user and outputs the average of all the numbers in the list.

num_list = input("Enter a list of numbers, separated by spaces: ").split()
num_list = [int(num) for num in num_list]
avg = sum(num_list) / len(num_list)
print("The average is:", avg)
