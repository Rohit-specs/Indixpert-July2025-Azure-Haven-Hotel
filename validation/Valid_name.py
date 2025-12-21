

import re
def valid_name(a="your"):
    while True:
        print("Please enter",a,"name: ",end="")
        name=input()
        if len(name)<3:
            print("There should be atleast 3 character\n")
        elif len(name)>25:
            print("Name should not bigger than 25 character\n")
        elif name[0]==" " or name[-1]==" ":
            print("Name must not start or end with a space\n")
        elif "  " in name:
            print("You entered extra space. please try again\n")
        elif re.search(r'[~!@#$%^&*]',name):
            print("Name does not contain any symbol\n")
        else:
            name=name.title()
            return name
            
  