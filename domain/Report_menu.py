
from report import Report_data

import domain
def report_menu():
    try:
        report_obj=Report_data()
        while True:
            print("\n-----------------Report_Menu-----------------")
            print("1. Total no. Of Booking")
            print("2. Current month no. of booking")
            print("3. Total Earning")
            print("4. Current Month Earning")
            print("5. Average Booking Duration")
            print("6. Current Month Average Booking Duration")
            print("7. Most Ordered item")
            print("8. Current Month Most Ordered item")
            print("9. Payment Method Used By Customer")
            print("10.Payment Method Used In Current Month By Customer")
            print("11.Back to Admin menu")
            try:
                choice=int(input("Enter your choice: "))
            except Exception as error:
                print("Invalid input. Please try again")
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
                print("Returning to Admin menu.")
                return

            else:
                print(choice,"is not a valid option")
    except Exception as error:
        print("Error occurred while loading Report Menu")
        log_obj=domain.log(error,__name__)

