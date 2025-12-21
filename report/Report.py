import json
import os
from collections import Counter

from domain import log

import datetime

class Report_data:
    def __init__(self):
        booked_table_file=os.path.join("database","booked_table.json")
        customer_order_file=os.path.join("database","customer_orders.json")
        payment_file=os.path.join("database","payment_file.json")
        with open(booked_table_file,'r') as data:
            try:
                self.table_booking_data=data.read()
            except Exception as error:
                log_obj=log(error,__name__)
                print("Error occurring while loading booked table json file.")
            
            try:
                self.table_booking_data=json.loads(self.table_booking_data)
            except Exception as error:
                log_obj=log(error,__name__)
                print("Please check if booked table is a valid json")
        # self.table_booking_data=file_reader(booked_table_file,__name__)


        with open(customer_order_file,'r') as data:
            try:
                self.customer_order_data=data.read()
            except Exception as error:
                log_obj=log(error,__name__)
                print("Error occurring while loading booked table json file.")
            try:
                self.customer_order_data=json.loads(self.customer_order_data)
            except Exception as error:
                log_obj=log(error,__name__)
                print("Please check if booked table is a valid json")
        # self.customer_order_data=file_reader(customer_order_file,__name__)


        with open(payment_file,'r') as data:
            try:
                self.payment_data=data.read()
            except Exception as error:
                log_obj=log(error,__name__)
                print("Error occurring while loading booked table json file.")
            try:
                self.payment_data=json.loads(self.payment_data)
            except Exception as error:
                log_obj=log(error,__name__)
                print("Please check if booked table is a valid json")
        # self.payment_data=file_reader(payment_file,__name__)

        current_month=str(datetime.datetime.now().month)
        self.modified_current_month="-"+current_month+"-"
    
    def no_of_booking(self):
        try:

            number_of_booking=len(self.table_booking_data)
            print(f"\nTotal number of booking: {number_of_booking}")
        except Exception as error:
            log_obj=log(error,__name__)
            print(f"Unexpected error: {error}")
    def current_number_of_booking(self):
        try:
            current_month_booking=0
            for booking in self.table_booking_data:
                month_booking=booking.get("table booking date")
                if self.modified_current_month in month_booking:
                    current_month_booking+=1  
            print(f"\nCurrent month number of booking: {current_month_booking}")
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)

    def average_booking_duration(self):
        try:
            number_of_booking=len(self.table_booking_data)
            if number_of_booking == 0:
                print("No bookings available for calculating average booking duration.")
                return

            average_booking_duration=0        
            for booking in self.table_booking_data:
                booking_duration=booking.get("booked time in min")

                average_booking_duration+=int(booking_duration)
            try:    
                average_booking_duration=average_booking_duration/number_of_booking
            except Exception as error:
                print(f"Unexpected Error: {error}")
                log_obj=log(error,__name__)
            print(f"\nAverage booking duration: {average_booking_duration}")
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)

    def current_month_average_booking_duration(self):

        try:
            current_month_average_booking_duration=0
            current_month_booking=0
            for booking in self.table_booking_data:

                booking_duration=booking.get("booked time in min")
                date=booking.get("table booking date")

                if self.modified_current_month in date:
                    current_month_booking+=1 
                    current_month_average_booking_duration+=booking_duration
            if current_month_booking == 0:
                print("No bookings available for calculating average booking duration.")
                return
            try:
                current_month_average_booking_duration=current_month_average_booking_duration/current_month_booking
            except Exception as error:
                print(f"Unexpected error: {error}")
                log_obj=log(error,__name__)
            print(f"\nCurrent month average booking duration: {current_month_average_booking_duration}")
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)

    def most_ordered_dish(self):
        
        try:
            all_order_list=[]
            for order in self.customer_order_data:
                data=order.get("ordered items")
                for i in data:
                    for key,value in i.items():
                        all_order_list.append(key)

            count=Counter(all_order_list)
            most_ordered_dish = count.most_common(1)[0][0]
            most_ordered_dish_count = count.most_common(1)[0][1]
            print(f"\nMost ordered dish: {most_ordered_dish} {most_ordered_dish_count}")
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)

    def current_month_most_ordered_dish(self):

        try:
            current_month_order_list=[]
            for i in self.customer_order_data:
                date=i.get("date")
                orders=i.get("ordered items")
                for order in orders:
                    for key,value in order.items():
                        if self.modified_current_month in date:
                            current_month_order_list.append(key)
            if len(current_month_order_list)==0:
                print("No order avialiable to determine most ordish ")
            count=Counter(current_month_order_list)
            current_month_most_ordered_dish=count.most_common(1)[0][0]
            current_month_most_ordered_dish_count=count.most_common(1)[0][1]
            print(f"\nMost ordered dish in current month: {current_month_most_ordered_dish} {current_month_most_ordered_dish_count}")
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)

    def payment_method_used(self):

        try:
            upi_count=0
            cash_count=0
            card_count=0
            for payment in self.payment_data:

                payment_method=payment.get("payment_method")
                if payment_method.lower()=="upi":
                    upi_count+=1
                elif payment_method.lower()=="card":
                    card_count+=1
                elif payment_method.lower()=="cash":
                    cash_count+=1
            print("\nPayment used by customers:-")
            print(f"Cash:  {cash_count} times")
            print(f"Card:  {card_count} times")
            print(f"UPI:   {upi_count} times")
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)

    def current_month_payment_method_used(self):

        try:
            monthly_upi_count=0
            monthly_card_count=0
            monthly_cash_count=0
            for payment in self.payment_data:
                date=payment.get("payment_date")
                if self.modified_current_month in date:
                    monthly_payment_method=payment.get("payment_method")
                    if monthly_payment_method.lower()=="upi":
                        monthly_upi_count+=1
                    elif monthly_payment_method.lower()=="card":
                        monthly_card_count+=1
                    elif monthly_payment_method.lower()=="cash":
                        monthly_cash_count+=1
            print("\nPayment method used in current month by customers:-")
            print(f"Cash: {monthly_cash_count} times")
            print(f"Card: {monthly_card_count} times")
            print(f"UPI:  {monthly_upi_count} times")
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)
    
    def total_revenue(self):

        try:
            revenue=0
            for payment in self.payment_data:
                amount=payment.get("total_amount")
                revenue+=float(amount)
            print("\nTotal Earning:",revenue)
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)

    def current_month_total_revenue(self):
        
        try:
            monthly_revenue=0
            for payment in self.payment_data:
                date=payment.get("payment_date")
                if self.modified_current_month in date:
                    amount=payment.get("total_amount")
                    monthly_revenue+=float(amount)
            print(f"\nCurrent month Total earning: {monthly_revenue}")
        except Exception as error:
            print(f"Unexpected error: {error}")
            log_obj=log(error,__name__)




