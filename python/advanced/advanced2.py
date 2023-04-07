#Write a function that can calculate the factorial of a given number using recursion.
#Factorial of a number (n!) is the product of all numbers smaller than it. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
num = 5
print(factorial(num)) # Output: 120
