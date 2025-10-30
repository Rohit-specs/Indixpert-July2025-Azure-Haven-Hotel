import os
import json
from validation import valid_password,valid_email,valid_name
import getpass
import domain
from colorama import init,Back,Fore,Style
init(autoreset=True)
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
                log_obj=domain.log(error,__name__)
                print(Fore.RED+"Error while opening the file")
        try:        
            with open(self.path,'r') as data:
                self.staff_data=json.loads(data.read())
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(Fore.RED+"Error while loading the file") 
        # self.staff_data=domain.file_reader(self.path,__name__)

    def save(self):
        try:
            with open(self.path,'w') as data:
                modified_data=json.dumps(self.staff_data,indent=3)
                data.write(modified_data)      
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(Fore.RED+"Error occurring while Updating staff data")
            
            
    def remove_staff(self):
        print(Fore.GREEN+"\n-------------REMOVING STAFF-------------")
        name=valid_name("staff")
        email=valid_email("staff")
        try:
            while True:
                self.role=input("Enter you role: ").lower()
                if self.role!="staff" and self.role!="admin":
                    print(Fore.RED"You have entered wrong role\nchoose between (staff/admin)")
                    continue
                break        
            for user in self.staff_data:
                if user["name"]==name:
                    if user["email"]==email:
                        if user.get("role")==self.role:
                            self.staff_data.remove(user)
                            self.save()
                            print(Fore.GREEN+"Staff removed successfully")
                        else:
                            print(Fore.RED+"Role mismatch")
                    else:
                        print(Fore.RED+"email not found in Record")
        except Exception as error:
            print(Fore.RED+"Error occurring while removing a staff")
            log_obj=domain.log(error,__name__)
            
                
    def add_staff(self):
        print(Fore.GREEN+"\n--------------ADDING STAFF--------------")
        name=valid_name("staff")
        email=valid_email("staff")
        while True:
            password=valid_password()
            while True:
                confirm_password=getpass.getpass("Please confirm your password: ")
                while True:
                    self.role=input("Enter you role: ").lower()
                    if self.role!="staff" and self.role!="admin":
                        print(Fore.RED+"You have entered wrong role\nchoose between (staff/admin)\n")
                        continue
                    break       
                if password==confirm_password:
                    new_staff={"name":name,"email":email,"password":password,"role":self.role}
                    self.staff_data.append(new_staff)
                    self.save()
                    print(Fore.GREEN+"Staff added successfully...")
                    return
                    
                else:
                    attempt-=1
                    if attempt==0:
                        print(Fore.RED+"No attempt left now")
                        choice=input("Do you want to create a password again(yes/no): ")
                        if choice.lower()=="yes":
                            break
                        elif choice.lower()=="no":
                            domain.admin_menu()
                        else:
                            print(Fore.GREEN+str(choice)+"is not a valid option")                            
                    else:        
                        print(Fore.YELLOW+Style.DIM+"you have now"+str(attempt)+"attempt left.")

    def staff_details(self):
        staff_count=1
       
        try:
            print(Fore.GREEN+"\n--------------ALL USERS--------------")
            for staff in self.staff_data:
                
                print()
                print(Fore.RED+"User-",staff_count)
                print("Name     : ",staff.get("name"))
                print("Email    : ",staff.get("email"))
                print("Password : ","*"*len(staff.get("password")))
                print("Role     : ",staff.get("role"))
                staff_count+=1
                
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(error)
            return


                        