from colorama import init,Fore,Back,Style
import domain

def staff_menu(name):
    while True:
        print(Fore.RED+"\n\t---------------STAFF_MENU---------------")
        print(Style.RESET_ALL+"1. Show Menu")
        print("2. Book Table")
        print("3. See All Booking")
        print("4. Take Order")
        print("5. See All Orders")
        print("6. Take Payment")
        print("7. Show Invoice")
        print("8. Cancel Booked Table")
        print("9. Log Out"+Fore.YELLOW)
        try:
            choice=int(input("Enter your choice: "))
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
                print(choice,"is not a valid option")
        except Exception as error:
            obj=domain.log(error,__name__)
            print("Unable to use this option"+Style.RESET_ALL)