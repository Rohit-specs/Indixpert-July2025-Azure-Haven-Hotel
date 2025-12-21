import domain
from validation import valid_email,valid_password

def user_details(): 
    print("\n-----------------SIGN_IN-----------------")
    email=valid_email()
    password=valid_password()
    domain.findinguser(email,password)
    return
    