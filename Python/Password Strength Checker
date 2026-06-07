
def password_check():
    strength = 0

    choice = input("Enter a password to check its strength: ")
    length = len(choice)
    has_upper = any(c.isupper() for c in choice)
    has_lower = any(c.islower() for c in choice)
    has_digit = any(c.isdigit() for c in choice)
    has_special = any(not c.isalnum() for c in choice)

    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1   
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    if strength == 5:
        print("Password Strength: Strong") 
    elif strength == 4: 
        print("Password Strength: Medium")
    elif strength >= 3: 
        print("Password Strength: Weak")
    else:
        print("Password Strength: Very Weak")

while True:
    password_check()