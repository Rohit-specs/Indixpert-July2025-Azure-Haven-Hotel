from colorama import init,Fore
init(autoreset=True)
import re
import getpass
def valid_password():
    while True:
        password=getpass.getpass("Enter your password(alphanumeric): ")
        if len(password)<6 and len(password)>20:
            print(Fore.RED+"password must contain at least 6 and maximum 20 digit and character\n")
        elif not re.search(r'[A-Z]',password):
            print(Fore.RED+"Password must contain a uppercase\n")
        elif not re.search(r'[a-z]',password):
            print(Fore.RED+"Password must contain a lowercase\n")
        elif not re.search(r'[@$%!*?&]',password):
            print(Fore.RED+"Password must contain a special character ex(@$%!*?&)\n")
        elif not re.search(r'[0-9]',password):
            print(Fore.RED+"Password must contain numbers\n")
        else:
            return password
        

