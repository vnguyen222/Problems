#Write a program that takes in a list of integers from the user and outputs the sum of all the even numbers in the list.

num_list = input("Enter a list of numbers, separated by spaces: ").split()
num_list = [int(num) for num in num_list]
sum = 0
for num in num_list:
    if num % 2 == 0:
        sum += num
print("The sum of all the even numbers is:", sum)
    