'''Write a function that takes in an email address and returns true if it’s properly formatted. For example, isValidEmail(“bigcharlie@gmail.com”) returns true but isValidEmail(“smallcharlie@gmail”) returns false
Test cases:'''

import re

def validate_email(email):
    # Define the regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the re module to match the email with the pattern
    match = re.match(pattern, email)
    
    # If the match is found, return True; otherwise, return False
    if match:
        return True
    else:
        return False
print(validate_email("bigcharlie@gmail.com")) 
print(validate_email("smallcharlie@gmail")) 
print(validate_email("your.fbi.agent@fbigov")) 
print(validate_email("yo.mama@nsa.gov")) 
print(validate_email("H@HA@gmail.com")) 
