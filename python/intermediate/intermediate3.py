#Write a method that takes in two numbers that represent hours worked and hourly pay. The function should return the total amount paid for the hours entered. For any hours over 40, you should receive overtime pay, which is 1.5 times the regular pay.

def calculate_pay(hours_worked, hourly_pay):
    if hours_worked <= 40:
        total_pay = hours_worked * hourly_pay
    else:
        regular_pay = 40 * hourly_pay
        overtime_pay = (hours_worked - 40) * (hourly_pay * 1.5)
        total_pay = regular_pay + overtime_pay
    return total_pay

# Example usage
print(calculate_pay(35, 10))  # Output: 350
print(calculate_pay(45, 10))  # Output: 475
