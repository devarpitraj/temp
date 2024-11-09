import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    '''
    ^:
    This asserts the start of the string. It ensures that the match must begin from the very beginning of the string.
    
    [a-zA-Z0-9._%+-]+:
    This matches the local part (before the @) of the email.
    [a-zA-Z0-9._%+-]: This is a character class that matches any of the following:
        Lowercase letters a-z
        Uppercase letters A-Z
        Digits 0-9
        Special characters ._%+-
    The + quantifier means "one or more" of the characters in this set, ensuring the local part of the email has at least one character.
    
    @:
    This matches the literal @ symbol. The @ separates the local part from the domain part of the email.
    
    [a-zA-Z0-9.-]+:

    This matches the domain part (after the @) of the email.
    [a-zA-Z0-9.-]: This character class matches:
        Lowercase letters a-z
        Uppercase letters A-Z
        Digits 0-9
        Dots (.) and hyphens (-) — commonly used in domain names.
    The + quantifier ensures that at least one of these characters appears, so the domain part can't be empty.
    
    \.:
    This matches the literal period (.) that separates the domain name from the top-level domain (TLD), like .com, .org, etc. The backslash \ is needed because the period is a special character in regex (it normally matches any character), so we escape it to match a literal dot.
    
    [a-zA-Z]{2,}:
    This matches the top-level domain (TLD).
    [a-zA-Z]: This character class matches uppercase or lowercase letters, which are valid characters in a TLD.
    {2,}: This quantifier means "at least 2" of the preceding characters (letters), ensuring that the TLD has at least two characters (which is the minimum for valid TLDs).
    
    $:
    This asserts the end of the string. It ensures that the match ends at the very last character of the string, meaning there are no extra characters after the email address.
    '''
    
    if re.match(pattern, email): return True
    else: return False

email = input("Enter email address: ")

print("Valid Email Address") if validate_email(email) else print("Invalid Email Address")