# import os
# import json
# import domain
# from authentication import users_details
# path="database/user_data.json"
# def menu():
#     while True:
#         flag=0
#         admin_flag=0
#         if not os.path.exists(path):
#             with open(path,'w') as file:
#                 data=[]
#                 json.dumps(data)
#                 file.write(data)
#         else:        
#             with open(path,'r') as f:
#                 data=f.read()
#                 data=json.loads(data)
#         if data==[]:
#             flag=1
#         for staff in data:
#             if not staff["role"]=="admin":
#                 admin_flag=1
        
#         print("--------AZURE HEAVEN HOTEL--------")
#         if flag==0:
#             print("1. Login")
#             print("2. Exit")
#         if flag==1:
#             print("1. Signup")
#             print("2. Login")
#             print("3. Exit")
#         choice=int(input("Enter your choice: "))
#         if choice==1 and flag==0:
#             users_details.user_details()

#         elif choice==2 and flag==0:
#             print("Exiting program...")
#             return

#         elif choice==1 and flag==1:
#             domain.Update_staff(path)

#         elif choice==2 and flag==1:
#             print("You haven't Signed yet")
#             print("There is not record in database of staff and admin")
#             print("Please signup")

#         elif choice==3 and flag==1:
#             print("Exiting program...")
#             return

#         else:
#             print("Not a valid option")

# import os
# import json
# from authentication import users_details
# import domain

# path = "database/user_data.json"

# def menu():
#     while True:
#         flag = 0
#         admin_flag = 0

#         if not os.path.exists(path):
#             with open(path, 'w') as file:
#                 list=[]
#                 json.dumps(list)
#                 file.write(list)

#         with open(path, 'r') as file:
#             try:
#                 data = json.loads(file.read())
#             except json.JSONDecodeError:
#                 data = []

#         if data == []:
#             flag = 0
#         else:
    
#             for staff in data:
#                 if staff["role"] == "admin":
#                     admin_flag = 1
#                     break

#         print("\n-------- AZURE HEAVEN HOTEL --------")
#         print("1. Signup")
#         print("2. Login")
#         print("3. Exit")

#         try:
#             choice = int(input("Enter your choice: "))
#         except ValueError:
#             print("Invalid input! Please enter a number")
#             continue

#         if choice == 1:
#             domain.update_staff(path)

#         elif choice == 2:
#             if data == []:
#                 print("No users have signed up yet. Please sign up first")
#                 continue
#             elif admin_flag == 0:
#                 print("No admin account found. Please register an admin first")
#                 continue
#             else:
#                 users_details.user_details()

#         elif choice == 3:
#             print("Exiting program...")
#             return

#         else:
#             print("Invalid option Please try again")

from colorama import init,Fore,Back,Style
import os
import json
from authentication import users_details
import domain
path = "database/user_data.json"

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
                obj=domain.log(error,__name__)

        if data != []:
            for staff in data:
                if "role" in staff and staff["role"] == "admin":
                    admin_flag = 1
                    break

        print(Fore.RED+"\n-----------------AZURE HEAVEN HOTEL-----------------"+Fore.GREEN)
        if admin_flag == 0:
            print("1. Signup")
            print("2. Signin")
            print("3. Exit")
        else:
            print("1. Login")
            print("2. Exit"+Fore.YELLOW)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError as error:
            print(Fore.BLUE+"Invalid input! Please enter a number")
            obj=domain.log(error,__name__)
            continue
        
        
        if admin_flag == 0:
            if choice == 1:
                    domain.update_staff(path)
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
