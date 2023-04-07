'''Develop a program that can determine whether a given year is a leap year or not.
A year is a leap year if:
It is divisible by 4.
It is not divisible by 100, unless...
It is divisible by 400.'''
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example usage
year = 2020
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Output: 2020 is a leap year.
