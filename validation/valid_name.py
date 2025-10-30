from colorama import init,Fore
init(autoreset=True)
import re
def valid_name(a="your"):
    while True:
        print("Please enter",a,"name: ",end="")
        name=input()
        if len(name)<3:
            print(Fore.RED+"There should be atleast 3 character\n")
        elif len(name)>25:
            print(Fore.RED+"Name should not bigger than 25 character\n")
        elif name[0]==" " or name[-1]==" ":
            print(Fore.RED+"Name must not start or end with a space\n")
        elif "  " in name:
            print(Fore.RED+"You entered extra space. please try again\n")
        elif re.search(r'[~!@#$%^&*]',name):
            print(Fore.RED+"Name does not contain any symbol\n")
        else:
            name=name.title()
            return name
            
  