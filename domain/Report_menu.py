from colorama import init,Fore,Style
from report import Report_data
init(autoreset=True)
import domain
def report_menu():
    try:
        obj=Report_data()
        while True:
            print(Fore.RED+Style.BRIGHT+"\n-----------------Report_Menu-----------------")
            print(Fore.CYAN+"1. ","Total no. Of Booking")
            print(Fore.CYAN+"2. ","Current month no. of booking")
            print(Fore.CYAN+"3. ","Total Earning")
            print(Fore.CYAN+"4. ","Current Month Earning")
            print(Fore.CYAN+"5. ","Average Booking Duration")
            print(Fore.CYAN+"6. ","Current Month Average Booking Duration")
            print(Fore.CYAN+"7. ","Most Ordered item")
            print(Fore.CYAN+"8. ","Current Month Most Ordered item")
            print(Fore.CYAN+"9. ","Payment Method Used By Customer")
            print(Fore.CYAN+"10.","Payment Method Used In Current Month By Customer")
            print(Fore.CYAN+"11.","Back to Admin menu")
            try:
                choice=int(input(Fore.YELLOW+"Enter your choice: "))
            except Exception as error:
                print(Fore.RED,"Invalid input. Please try again")
                obj=domain.log(error,__name__)
                continue
            if choice==1:
                obj.no_of_booking()
            
            elif choice==2:
                obj.current_number_of_booking()
            
            elif choice==3:
                obj.total_revenue()

            elif choice==4:
                obj.current_month_total_revenue()

            elif choice==5:
                obj.average_booking_duration()

            elif choice==6:
                obj.current_month_average_booking_duration()

            elif choice==7:
                obj.most_ordered_dish()

            elif choice==8:
                obj.current_month_most_ordered_dish()
            
            elif choice==9:
                obj.payment_method_used()

            elif choice==10:
                obj.current_month_payment_method_used()

            elif choice==11:
                print(Fore.YELLOW+"Returning to Admin menu.")
                return

            else:
                print(Fore.RED+choice,"is not a valid option")
    except Exception as error:
        print(Fore.RED+"Error occurred while loading Report Menu")
        obj=domain.log(error,__name__)

