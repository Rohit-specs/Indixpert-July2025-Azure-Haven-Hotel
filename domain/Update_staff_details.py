import os
import json
from validation import valid_password,valid_email,valid_name
import getpass
import domain
from colorama import init,Back,Fore,Style
class update_staff:
    attempt=4
    def __init__(self,path):
        self.path=path
        
        if not os.path.exists(self.path):
            try:
                with open(self.path,'w') as file:
                    data=[] 
                    json.dumps(data)
                    file.write(data)
            except Exception as error:
                obj=domain.log(error,__name__)
                print("Error while opening the file")
        try:        
            with open(self.path,'r') as data:
                self.staff_data=json.loads(data.read())
        except Exception as error:
            obj=domain.log(error,__name__)
            print("Error while loading the file") 

    def save(self):
        try:
            with open(self.path,'w') as data:
                modified_data=json.dumps(self.staff_data,indent=3)
                data.write(modified_data)      
        except Exception as error:
            obj=domain.log(error,__name__)
            print("Error occurring while Updating staff data")
            
            
    def remove_staff(self):
        print(Fore.GREEN+"\n-------------REMOVING STAFF-------------"+Fore.YELLOW)
        name=valid_name("staff")
        email=valid_email("staff")
        try:
            while True:
                self.role=input("Enter you role: ")
                if self.role!="staff" and self.role!="admin":
                    print("You have entered wrong role\nchoose between (staff/admin)")
                    continue
                break        
            for user in self.staff_data:
                if user["name"]==name:
                    if user["email"]==email:
                        if user.get("role")==self.role:
                            self.staff_data.remove(user)
                            self.save()
                            print("Staff removed successfully")
                        else:
                            print("Role mismatch")
                    else:
                        print("email not found in Record")
        except Exception as error:
            print("Error occurring while removing a staff")
            obj=domain.log(error,__name__)
            
                
    def add_staff(self):
        print(Fore.GREEN+"\n--------------ADDING STAFF--------------"+Fore.YELLOW)
        name=valid_name("staff")
        email=valid_email()
        while True:
            password=valid_password()
            while True:
                confirm_password=getpass.getpass("Please confirm your password: ")
                while True:
                    self.role=input("Enter you role: ")
                    if self.role!="staff" and self.role!="admin":
                        print("You have entered wrong role\nchoose between (staff/admin)")
                        continue
                    break       
                if password==confirm_password:
                    new_staff={"name":name,"email":email,"password":password,"role":self.role}
                    self.staff_data.append(new_staff)
                    self.save()
                    print("Staff added successfully...")
                    return
                    
                else:
                    attempt-=1
                    if attempt==0:
                        print("No attempt left now")
                        choice=input("Do you want to create a password again(yes/no): ")
                        if choice.lower()=="yes":
                            break
                        elif choice.lower()=="no":
                            domain.admin_menu()
                        else:
                            print(choice,"is not a valid option")                            
                    else:        
                        print("you have now",attempt,"attempt left.")

    def staff_data():
        i=1
        # json_path=os.path.join("database","user_data.json")
        # try:
        #     with open(json_path,'r') as user_data:
        #         Staffs=json.loads(user_data.read())
        # except Exception as error:
        #     obj=domain.log(error,__name__)
        #     print(Fore.RED+"File Not Found In Database")
        #     return
        try:
            print(Fore.GREEN+"--------------ALL USERS--------------")
            for staff in self.staff_data:
                print(Fore.RED+"User-",i)
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


                        