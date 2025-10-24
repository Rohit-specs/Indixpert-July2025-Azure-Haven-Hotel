from colorama import init,Fore,Back,Style
import domain
import os
def admin_menu():
    while True:
        print(Fore.RED+Style.BRIGHT+"\n\t--------------ADMIN_MENU--------------")
        print(Style.RESET_ALL+"1. Menu")
        print("2. Delete Dish")
        print("3. Add Dish")
        print("4. Add New Category")
        print("5. Delete Category")
        print("6. Update Dish Price")
        print("7. Add Staff Member")
        print("8. Remove Staff Member")
        print("9. Show Staff")
        print("10. Log Out"+Fore.YELLOW)
        
        try:
            choice=int(input("Enter Your Choice: "))
        except Exception as error:
            print(error)
            obj=domain.log(error,__name__)
            continue

        path=os.path.join("database","menu.json")
        path1=os.path.join("database","user_data.json")
        
        try:
            if choice==1:
                obj=domain.show_menu()
            elif choice==2:
                obj1=domain.update_menu(path)
                obj1.delete_dish()
            elif choice==3:
                obj1=domain.update_menu(path)
                obj1.add_dish()
            elif choice==4:
                obj1=domain.update_menu(path)
                obj1.add_category()
            elif choice==5:
                obj1=domain.update_menu(path)
                obj1.del_category()
            elif choice==6:
                obj1=domain.update_menu(path)
                obj1.update_price()
            elif choice==7:
                obj2=domain.update_staff(path1)
                obj2.add_staff()
            elif choice==8:
                obj2=domain.update_staff(path1)
                obj2.remove_staff()
            elif choice==9:
                domain.staff_data()
            elif choice==10:
                print("Exiting Admin Menu...")
                break
            else:
                print(choice,"is not a valid option")
        except Exception as error:
            print(error)
            ob=domain.log(error,__name__)
            continue