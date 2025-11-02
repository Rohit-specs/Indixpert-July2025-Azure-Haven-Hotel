from colorama import init,Fore,Back,Style
init(autoreset=True)
import domain

def staff_menu(name):
    while True:
        print(Fore.RED+"\n-------------------STAFF_MENU-------------------")
        print(Fore.CYAN+"1.","Show Menu")
        print(Fore.CYAN+"2.","Book Table")
        print(Fore.CYAN+"3.","View Booking")
        print(Fore.CYAN+"4.","Take Order")
        print(Fore.CYAN+"5.","View Orders")
        print(Fore.CYAN+"6.","Take Payment")
        print(Fore.CYAN+"7.","Show Invoice")
        print(Fore.CYAN+"8.","Cancel Booked Table")
        print(Fore.CYAN+"9.","Log Out")
        try:
            choice=int(input(Fore.YELLOW+"Enter your choice: "))
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print("Invalid input. Please enter a valid option")
            continue
        try:
            if choice==1:
                menu=domain.show_menu()
            elif choice==2:
                table_booking_object=domain.tablebooking().book_table(name)
            elif choice==3:
                table_booking_object=domain.tablebooking().show_booking_menu()
            elif choice==4:
                table_booking_object=domain.tablebooking().take_order()
            elif choice==5:
                table_booking_object=domain.tablebooking().show_order_menu()
            elif choice==6:
                table_booking_object=domain.tablebooking().payment()
            elif choice==7:
                table_booking_object=domain.tablebooking().get_invoice()
            elif choice==8:
                table_booking_object=domain.tablebooking().cancel_booking()
            elif choice==9:
                print("Exiting Staff Menu...")
                break
            else:
                print(Fore.RED+choice,"is not a valid option")
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(Fore.RED+"Unable to use this option")