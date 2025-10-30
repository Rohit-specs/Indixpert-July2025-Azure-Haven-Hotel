from colorama import init,Fore
init(autoreset=True)
def valid_email(option="your"):
    while True:
        print("Please enter",option,"email id: ",end="")
        email=input()
        if not email.endswith("@gmail.com"):
            print(Fore.RED+"email must contain @gmail.com at last!\n")
        elif email[0]==" " or email[-1]==" ":
            print(Fore.RED+"space in the first and last index\n")
        else:
            return email