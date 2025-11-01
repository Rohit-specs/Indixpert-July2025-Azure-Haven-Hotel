from colorama import init,Fore,Back,Style
init(autoreset=True)
from domain import log,update_menu,update_staff,show_menu,update_pricing_structure
import os
def admin_menu():
    menu_file_path=os.path.join("database","menu.json")
    user_file_path=os.path.join("database","user_data.json")
    update_menu_obj=update_menu(menu_file_path)
    update_staff_obj=update_staff(user_file_path)
    price_and_discount_management_obj=update_pricing_structure()
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
        print(Fore.CYAN+"10.","Price and Discount Management")
        print(Fore.CYAN+"11.","Report")
        print(Fore.CYAN+"12.","Log Out")
        
        try:
            choice=int(input(Fore.YELLOW+"Enter Your Choice: "))
        except Exception as error:
            print(error)
            log_obj=domain.log(error,__name__)
            continue

        try:
            if choice==1:
                menu_obj=show_menu()
            elif choice==2:
                update_menu_obj.delete_dish()
            elif choice==3:
                update_menu_obj.add_dish()
            elif choice==4:
                update_menu_obj.add_category()
            elif choice==5:
                update_menu_obj.del_category()
            elif choice==6:
                update_menu_obj.update_price()
            elif choice==7:
                update_staff_obj.add_staff()
            elif choice==8:
                update_staff_obj.remove_staff()
            elif choice==9:
                update_staff_obj.staff_details()
            elif choice==10:
                price_and_discount_management_obj.update_price_menu()
            elif choice==11:
                domain.report_menu()
            elif choice==12:
                print(Fore.RED,"Exiting Admin Menu...")
                break
            else:
                print(Fore.RED,choice,"is not a valid option")
        except Exception as error:
            print(error)
            log_obj=domain.log(error,__name__)
            continue