from colorama import init,Fore,Back,Style
init(autoreset=True)
import domain
import os
def admin_menu():
    path=os.path.join("database","menu.json")
    path1=os.path.join("database","user_data.json")
    obj1=domain.update_menu(path)
    obj2=domain.update_staff(path1)
    while True:
        print(Fore.RED+"\n-------------------ADMIN_MENU-------------------")
        print(Fore.CYAN+"1. ","Menu")
        print(Fore.CYAN+"2. ","Delete Dish")
        print(Fore.CYAN+"3. ","Add Dish")
        print(Fore.CYAN+"4. ","Add New Category")
        print(Fore.CYAN+"5. ","Delete Category")
        print(Fore.CYAN+"6. ","Update Dish Price")
        print(Fore.CYAN+"7. ","Add Staff Member")
        print(Fore.CYAN+"8. ","Remove Staff Member")
        print(Fore.CYAN+"9. ","Show Staff")
        print(Fore.CYAN+"10.","Report")
        print(Fore.CYAN+"11.","Log Out")
        
        try:
            choice=int(input(Fore.YELLOW+"Enter Your Choice: "))
        except Exception as error:
            print(error)
            obj=domain.log(error,__name__)
            continue

        try:
            if choice==1:
                obj=domain.show_menu()
            elif choice==2:
                obj1.delete_dish()
            elif choice==3:
                obj1.add_dish()
            elif choice==4:
                obj1.add_category()
            elif choice==5:
                obj1.del_category()
            elif choice==6:
                obj1.update_price()
            elif choice==7:
                obj2.add_staff()
            elif choice==8:
                obj2.remove_staff()
            elif choice==9:
                # domain.staff_data()
                obj2.staff_details()
            elif choice==10:
                domain.report_menu()
            elif choice==11:
                print(Fore.RED,"Exiting Admin Menu...")
                break
            else:
                print(Fore.RED,choice,"is not a valid option")
        except Exception as error:
            print(error)
            ob=domain.log(error,__name__)
            continue