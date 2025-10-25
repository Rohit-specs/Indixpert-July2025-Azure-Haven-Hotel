import json
import os
import domain


json_path=os.path.join("database","user_data.json")
def findinguser(email,password):
    try:
        with open(json_path,'r') as file:
            users=file.read()
            users=json.loads(users)
    except Exception as error:
        obj=domain.log(error,__name__)
        print("Error While Loading User Wata")
        return
    
    try:
        for user in users:
            name=str(user["name"])
            if user.get("email") == email:
                if user.get("password") == password:
                    if user.get("role") == "admin":
                        domain.admin_menu()
                        return
                        
                    elif user.get("role") == "staff":
                        domain.staff_menu(name)
                        return
                else:
                    print("You entered wrong password")
                    return
    except Exception as error:
        print(error)
        obj=domain.log(error,__name__)
        return
    print("user not found")