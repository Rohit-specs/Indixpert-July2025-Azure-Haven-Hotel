import re
import getpass
def valid_password():
    while True:
        password=getpass.getpass("Enter your password(alphanumeric): ")
        if len(password)<6 and len(password)>20:
            print("password must contain at least 6 and maximum 20 digit and character")
        elif not re.search(r'[A-Z]',password):
            print("Password must contain a uppercase")
        elif not re.search(r'[a-z]',password):
            print("Password must contain a lowercase")
        elif not re.search(r'[@$%!*?&]',password):
            print("Password must contain a special character ex(@$%!*?&)")
        elif not re.search(r'[0-9]',password):
            print("Password must contain numbers")
        else:
            return password
        

