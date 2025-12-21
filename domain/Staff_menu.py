

import domain

def staff_menu(name):
    while True:
        print("\n-------------------STAFF_MENU-------------------")
        print("1. Show Menu")
        print("2. Book Table")
        print("3. View Booking")
        print("4. Take Order")
        print("5. View Orders")
        print("6. Take Payment")
        print("7. Show Invoice")
        print("8. Cancel Booked Table")
        print("9. Log Out")
        try:
            choice=int(input("Enter your choice: "))
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
                print(choice,"is not a valid option")
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print("Unable to use this option")