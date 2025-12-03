import domain
from validation import valid_email,valid_password
from colorama import init,Fore,Style,Back
def user_details(): 
    print(Fore.GREEN+"\n-----------------SIGN_IN-----------------")
    email=valid_email()
    password=valid_password()
    domain.findinguser(email,password)
    return
    