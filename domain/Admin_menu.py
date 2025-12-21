

import domain
import os
def admin_menu():
    menu_file_path=os.path.join("database","menu.json")
    user_file_path=os.path.join("database","user_data.json")
    update_menu_obj=domain.update_menu(menu_file_path)
    update_staff_obj=domain.update_staff(user_file_path)
    price_and_discount_management_obj=domain.update_pricing_structure()
    while True:
        print("\n-------------------ADMIN_MENU-------------------")
        print("1. Menu")
        print("2. Delete Dish")
        print("3. Add Dish")
        print("4. Add New Category")
        print("5. Delete Category")
        print("6. Update Dish Price")
        print("7. Add Staff Member")
        print("8. Remove Staff Member")
        print("9. Show Staff")
        print("10.Price and Discount Management")
        print("11.Report")
        print("12.Log Out")
        
        try:
            choice=int(input("Enter Your Choice: "))
        except Exception as error:
            print(error)
            log_obj=domain.log(error,__name__)
            continue

        try:
            if choice==1:
                menu_obj=domain.show_menu()
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
                print("Exiting Admin Menu...")
                break
            else:
                print(choice,"is not a valid option")
        except Exception as error:
            print(error)
            log_obj=domain.log(error,__name__)
            continue