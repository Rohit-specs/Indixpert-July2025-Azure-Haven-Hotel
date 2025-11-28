
from colorama import init,Fore,Back,Style
import os
import json
from authentication import users_details
import domain
path=os.path.join("database","user_data.json")

def menu():
    while True:
        admin_flag = 0
        
        if not os.path.exists(path):
            with open(path, 'w') as file:
                file.write(json.dumps([]))  
        
        with open(path, 'r') as file:
            try:
                data = json.loads(file.read())
            except json.JSONDecodeError as error:
                data = []
                log_obj=domain.log(error,__name__)

        if data != []:
            for staff in data:
                if "role" in staff and staff["role"] == "admin":
                    admin_flag = 1
                    break

        print(Fore.RED+"\n-----------------AZURE HEAVEN HOTEL-----------------")
        if admin_flag == 0:
            print(Fore.GREEN+"1. Signup"+Style.RESET_ALL)
            print(Fore.GREEN+"2. Signin"+Style.RESET_ALL)
            print(Fore.GREEN+"3. Exit"+Style.RESET_ALL)
        else:
            print(Fore.GREEN+"1. Login"+Style.RESET_ALL)
            print(Fore.GREEN+"2. Exit"+Style.RESET_ALL)
        try:
            choice = int(input(Fore.YELLOW+"Enter your choice: "))
        except ValueError as error:
            print(Fore.RED+"Invalid input! Please enter a number")
            log_obj=domain.log(error,__name__)
            continue
        
        
        if admin_flag == 0:
            if choice == 1:
                    signup_obj=domain.update_staff(path).add_staff()
            elif choice == 2:
                if data == []:
                    print("No users have signed up yet. Please sign up first")
                else:
                    users_details.user_details()
            elif choice == 3:
                print("Exiting program...")
                return
            else:
                print("Invalid option. Please try again")
        else:
            if choice == 1:
                users_details.user_details()
            elif choice == 2:
                print("Exiting program...")
                return
            else:
                print("Invalid option. Please try again")
