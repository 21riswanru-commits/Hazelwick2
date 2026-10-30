
def is_valid_password(password):
    if len(password)>=8:
        hasupper=any(upper.isupper()for upper in password)
        hasdigit=any(digit.isdigit()for digit in password)
        return hasupper and hasdigit
    else:
        return False

valid=False
while valid==False:
    password=input("Enter a password:")
    if is_valid_password(password):
        print("password accepted")
        valid=True
    else:
        print("password must be at least 8 characters with one uppercase letter and one digit")
        
