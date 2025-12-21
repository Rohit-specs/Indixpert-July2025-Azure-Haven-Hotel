import os
import json
from validation import valid_password,valid_email,valid_name
import getpass
import domain

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
                print("Error while opening the file")
        try:        
            with open(self.path,'r') as data:
                self.staff_data=json.loads(data.read())
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print("Error while loading the file") 

    def save(self):
        try:
            with open(self.path,'w') as data:
                modified_data=json.dumps(self.staff_data,indent=3)
                data.write(modified_data)      
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print("Error occurring while Updating staff data")
            
            
    def remove_staff(self):
        print("\n-------------REMOVING STAFF-------------")
        name=valid_name("staff")
        email=valid_email("staff")
        try:
            while True:
                self.role=input("Enter you role: ").lower()
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
            log_obj=domain.log(error,__name__)
            
                
    def add_staff(self):
        print("\n--------------ADDING STAFF--------------")
        name=valid_name("staff")
        email=valid_email("staff")
        while True:
            password=valid_password()
            while True:
                confirm_password=getpass.getpass("Please confirm your password: ")
                while True:
                    self.role=input("Enter you role: ").lower()
                    if self.role!="staff" and self.role!="admin":
                        print("You have entered wrong role\nchoose between (staff/admin)\n")
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
                            print(str(choice)+"is not a valid option")                            
                    else:        
                        print(Style.DIM+"you have now"+str(attempt)+"attempt left.")

    def staff_details(self):
       
        try:
            print("\n--------------ALL USERS--------------")
            for staff_count,staff in enumerate(self.staff_data,1):
                
                print()
                print(f"User-  {staff_count}")
                print(f"Name     :  {staff.get('name')}")
                print(f"Email    :  {staff.get('email')}")
                print(f"Password :  {'*'*len(staff.get('password'))}")
                print(f"Role     :  {staff.get('role')}")
                
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(error)
            return


                        