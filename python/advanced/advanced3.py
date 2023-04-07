#Build a program that can generate the Fibonacci series up to a given number of terms.
#The Fibonacci series is a series of numbers where each number is the sum of the previous two numbers, starting with 0 and 1. 
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …
#fibonacci(10) returns a list of the first ten fibonacci numbers, which is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def fibonacci(num_terms):
    # Initialize the first two terms of the series
    a, b = 0, 1
    
    # Create an empty list to store the series
    fib_series = []
    
    # Generate the series up to the given number of terms
    for i in range(num_terms):
        fib_series.append(a)
        a, b = b, a + b
        
    return fib_series

# Example usage
num_terms = 10
print(fibonacci(num_terms)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
