import domain
import json
import os
from colorama import init,Fore,Back,Style
def staff_data():
    i=1
    json_path=os.path.join("database","user_data.json")
    try:
        with open(json_path,'r') as user_data:
            Staffs=json.loads(user_data.read())
    except Exception as error:
        obj=domain.log(error,__name__)
        print("File Not Found In Database")
        return
    try:
        print(Fore.GREEN+"--------------ALL USERS--------------")
        for staff in Staffs:
            print(Fore.RED+"User-",i,Fore.CYAN)
            print("Name     : ",staff.get("name"))
            print("Email    : ",staff.get("email"))
            print("Password : ","*"*len(staff.get("password")))
            print("Role     : ",staff.get("role"))
            print()
            i+=1
    except Exception as error:
        obj=domain.log(error,__name__)
        print(error)
        return
