#Write a method is_tired that states if the user is tired or not. A user is tired if the amount of sleep they got is less than 8 hours. If they’ve slept at least 5 hours, but have had coffee, the user is not tired
def is_tired(hours_of_sleep, has_coffee):
    if hours_of_sleep < 8 and not has_coffee:
        return True
    elif hours_of_sleep >= 5 and has_coffee:
        return False
    else:
        return False

# Example usage
print(is_tired(7, True))   # Output: False
print(is_tired(4, False))  # Output: True
print(is_tired(9, False))  # Output: False
