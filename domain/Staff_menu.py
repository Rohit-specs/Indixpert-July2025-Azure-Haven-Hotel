from colorama import init,Fore,Back,Style
init(autoreset=True)
import domain

def staff_menu(name):
    while True:
        print(Fore.RED+Style.BRIGHT+"\n-------------------STAFF_MENU-------------------")
        print(Fore.CYAN+"1.","Show Menu")
        print(Fore.CYAN+"2.","Book Table")
        print(Fore.CYAN+"3.","See All Booking")
        print(Fore.CYAN+"4.","Take Order")
        print(Fore.CYAN+"5.","See All Orders")
        print(Fore.CYAN+"6.","Take Payment")
        print(Fore.CYAN+"7.","Show Invoice")
        print(Fore.CYAN+"8.","Cancel Booked Table")
        print(Fore.CYAN+"9.","Log Out")
        try:
            choice=int(input(Fore.YELLOW+"Enter your choice: "))
        except Exception as error:
            log=domain.log(error,__name__)
            print("Invalid input. Please enter a valid option")
            continue
        try:
            if choice==1:
                menu=domain.show_menu()
            elif choice==2:
                obj=domain.tablebooking().book_table(name)
            elif choice==3:
                obj=domain.tablebooking().show_all_booking()
            elif choice==4:
                obj=domain.tablebooking().take_order()
            elif choice==5:
                obj=domain.tablebooking().show_all_orders()
            elif choice==6:
                obj=domain.tablebooking().payment()
            elif choice==7:
                obj=domain.tablebooking().get_invoice()
            elif choice==8:
                obj=domain.tablebooking().cancel_booking()
            elif choice==9:
                print("Exiting Staff Menu...")
                break
            else:
                print(Fore.RED+choice,"is not a valid option")
        except Exception as error:
            obj=domain.log(error,__name__)
            print(Fore.RED+"Unable to use this option")