from report import Report_data
def report_menu():
    while True:
        print("\n-----------------Report_Menu-----------------")
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
        # try:
        choice=int(input("Enter your choice: "))
        # except Exception as error:
        #     print("Invalid input. Please try again")
        #     obj=domain.log(error,__name__)
        #     continue
        if choice==1:
            obj=Report_data()
            obj.no_of_booking()
        
        elif choice==2:
            obj=Report_data()
            obj.current_number_of_booking()
        
        elif choice==3:
            obj=Report_data()
            obj.total_revenue()

        elif choice==4:
            obj=Report_data()
            obj.current_month_total_revenue()

        elif choice==5:
            obj=Report_data()
            obj.average_booking_duration()

        elif choice==6:
            obj=Report_data()
            obj.current_month_average_booking_duration()

        elif choice==7:
            obj=Report_data()
            obj.most_ordered_dish()

        elif choice==8:
            obj=Report_data()
            obj.current_month_most_ordered_dish()
        
        elif choice==9:
            obj=Report_data()
            obj.most_ordered_dish()

        elif choice==10:
            obj=Report_data()
            obj.current_month_payment_method_used()

        elif choice==11:
            return

        else:
            print(choice,"is not a valid option")

