from colorama import init,Fore,Style
from report import Report_data
init(autoreset=True)
import domain
def report_menu():
    try:
        obj=Report_data()
        while True:
            print(Fore.RED,Style.BRIGHT,"\n-----------------Report_Menu-----------------")
            print("1.  Total no. Of Booking")
            print("2.  Current month no. of booking")
            print("3.  Total Earning")
            print("4.  Current Month Earning")
            print("5.  Average Booking Duration")
            print("6.  Current Month Average Booking Duration")
            print("7.  Most Ordered item")
            print("8.  Current Month Most Ordered item")
            print("9.  Payment Method Used By Customer")
            print("10. Payment Method Used In Current Month By Customer")
            print("11. Back to Admin menu")
            try:
                choice=int(input("Enter your choice: "))
            except Exception as error:
                print("Invalid input. Please try again")
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
                obj.most_ordered_dish()

            elif choice==10:
                obj.current_month_payment_method_used()

            elif choice==11:
                print(Fore.YELLOW+"Returning to Admin menu.")
                return

            else:
                print(Fore.YELLOW,choice,"is not a valid option")
    except Exception as error:
        print("Error occurred while loading Report Menu")
        obj=domain.log(error,__name__)

