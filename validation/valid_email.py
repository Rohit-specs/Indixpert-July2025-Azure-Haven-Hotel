def valid_email():
    while True:
        email=input("Please enter your email id: ")
        if not email.endswith("@gmail.com"):
            print("email must contain @gmail.com at last!")
        elif email[0]==" " or email[-1]==" ":
            print("space in the first and last index")
        else:
            return email