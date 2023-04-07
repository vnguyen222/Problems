#Write a method called LuckyThirteen that takes in two values and returns whichever number is closest to 13 without going over the value 13. 
#For example, luckythirteen(9, 12) would return 12, whereas luckyThirteen(1,4) would return 4. If both values are above 13, then return the value 0. 

def lucky_thirteen(a, b):
    if a > 13 and b > 13:
        return 0
    elif a > 13:
        return b
    elif b > 13:
        return a
    elif abs(13 - a) <= abs(13 - b):
        return a
    else:
        return b

# Example usage
print(lucky_thirteen(9, 12))  # Output: 12
print(lucky_thirteen(1, 4))   # Output: 4
print(lucky_thirteen(14, 15)) # Output: 0
#code that writes itself
#Write a function called write_code that takes in a string and a number and returns a string that is the string repeated the number of times.