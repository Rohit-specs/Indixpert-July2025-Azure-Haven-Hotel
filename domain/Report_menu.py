from colorama import init,Fore,Style
from report import Report_data
init(autoreset=True)
import domain
def report_menu():
    try:
        report_obj=Report_data()
        while True:
            print(Fore.RED+"\n-----------------Report_Menu-----------------")
            print(Fore.CYAN+"1. "+Style.RESET_ALL+"Total no. Of Booking")
            print(Fore.CYAN+"2. "+Style.RESET_ALL+"Current month no. of booking")
            print(Fore.CYAN+"3. "+Style.RESET_ALL+"Total Earning")
            print(Fore.CYAN+"4. "+Style.RESET_ALL+"Current Month Earning")
            print(Fore.CYAN+"5. "+Style.RESET_ALL+"Average Booking Duration")
            print(Fore.CYAN+"6. "+Style.RESET_ALL+"Current Month Average Booking Duration")
            print(Fore.CYAN+"7. "+Style.RESET_ALL+"Most Ordered item")
            print(Fore.CYAN+"8. "+Style.RESET_ALL+"Current Month Most Ordered item")
            print(Fore.CYAN+"9. "+Style.RESET_ALL+"Payment Method Used By Customer")
            print(Fore.CYAN+"10."+Style.RESET_ALL+"Payment Method Used In Current Month By Customer")
            print(Fore.CYAN+"11."+Style.RESET_ALL+"Back to Admin menu")
            try:
                choice=int(input(Fore.YELLOW+"Enter your choice: "))
            except Exception as error:
                print(Fore.RED,"Invalid input. Please try again")
                log_obj=domain.log(error,__name__)
                continue
            if choice==1:
                report_obj.no_of_booking()
            
            elif choice==2:
                report_obj.current_number_of_booking()
            
            elif choice==3:
                report_obj.total_revenue()

            elif choice==4:
                report_obj.current_month_total_revenue()

            elif choice==5:
                report_obj.average_booking_duration()

            elif choice==6:
                report_obj.current_month_average_booking_duration()

            elif choice==7:
                report_obj.most_ordered_dish()

            elif choice==8:
                report_obj.current_month_most_ordered_dish()
            
            elif choice==9:
                report_obj.payment_method_used()

            elif choice==10:
                report_obj.current_month_payment_method_used()

            elif choice==11:
                print(Fore.YELLOW+"Returning to Admin menu.")
                return

            else:
                print(Fore.RED+choice,"is not a valid option")
    except Exception as error:
        print(Fore.RED+"Error occurred while loading Report Menu")
        log_obj=domain.log(error,__name__)

