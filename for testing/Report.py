import json
import os
# from domain import log
from collections import Counter
import datetime
booked_table_file=os.path.join("database","booked_table.json")
customer_order_file=os.path.join("database","customer_orders.json")
payment_file=os.path.join("database","payment_file.json")
with open(booked_table_file,'r') as data:
    # try:
    table_booking_data=data.read()
    # except Exception as error:
    #     obj=log(error,__name__)
    #     print("Error occurring while loading booked table json file.")
    # try:
    table_booking_data=json.loads(table_booking_data)
    # except Exception as error:
    #     obj=log(error,__name__)
    #     print("Please check if booked table is a valid json")


with open(customer_order_file,'r') as data:
    # try:
    customer_order_data=data.read()
    # except Exception as error:
    #     obj=log(error,__name__)
    #     print("Error occurring while loading booked table json file.")
    # try:
    customer_order_data=json.loads(customer_order_data)
    # except Exception as error:
    #     obj=log(error,__name__)
    #     print("Please check if booked table is a valid json")


with open(payment_file,'r') as data:
    # try:
    payment_data=data.read()
    # except Exception as error:
        # obj=log(error,__name__)
        # print("Error occurring while loading booked table json file.")
    # try:
    payment_data=json.loads(payment_data)
    # except Exception as error:
    #     obj=log(error,__name__)
    #     print("Please check if booked table is a valid json")

print("********************REPORT********************")    

average_booking_duration=0        
current_month_booking=0
current_month_average_booking_duration=0
number_of_booking=len(table_booking_data)
current_month=str(datetime.datetime.now().month)
modified_current_month="-"+current_month+"-"

for booking in table_booking_data:
    booking_duration=booking.get("booked time in min")
    
    average_booking_duration+=int(booking_duration)
    
    month_booking=booking.get("table booking date")
    if modified_current_month in month_booking:
        current_month_booking+=1 
        current_month_average_booking_duration+=booking_duration  
   

average_booking_duration=average_booking_duration/number_of_booking
current_month_average_booking_duration=current_month_average_booking_duration/current_month_booking
print("\nTotal number of booking",number_of_booking)
print("Current month number of booking:",current_month_booking)
print("\nAverage booking duration:",average_booking_duration,"minute")
print("Current month average booking duration:",current_month_average_booking_duration,"minute")


all_order_list=[]
for order in customer_order_data:
    data=order.get("ordered items")
    for i in data:
        for key,value in i.items():
            all_order_list.append(key)
print("\nMost ordered dish:",end=" ")

count=Counter(all_order_list)
most_ordered_dish = count.most_common(1)[0][0]
most_ordered_dish_count = count.most_common(1)[0][1]
print(most_ordered_dish,"(x"+str(most_ordered_dish_count)+")")

current_month_order_list=[]
for i in customer_order_data:
    date=i.get("date")
    orders=i.get("ordered items")
    for order in orders:
        for key,value in order.items():
            if modified_current_month in date:
                current_month_order_list.append(key)
count=Counter(current_month_order_list)
current_month_most_ordered_dish=count.most_common(1)[0][0]
current_month_most_ordered_dish_count=count.most_common(1)[0][1]
print("Most ordered dish in current month:",current_month_most_ordered_dish,"(X"+str(current_month_most_ordered_dish_count)+")")
 

revenue=0
upi_count=0
cash_count=0
card_count=0
for payment in payment_data:
    amount=payment.get("total_amount")
    revenue+=float(amount)

    payment_method=payment.get("payment_method")
    if payment_method.lower()=="upi":
        upi_count+=1
    elif payment_method.lower()=="card":
        card_count+=1
    elif payment_method.lower()=="cash":
        cash_count+=1
    


monthly_revenue=0
monthly_upi_count=0
monthly_card_count=0
monthly_cash_count=0
for payment in payment_data:
    date=payment.get("payment_date")
    if modified_current_month in date:
        amount=payment.get("total_amount")
        monthly_revenue+=float(amount)
        monthly_payment_method=payment.get("payment_method")
        if monthly_payment_method.lower()=="upi":
            monthly_upi_count+=1
        elif monthly_payment_method.lower()=="card":
            monthly_card_count+=1
        elif monthly_payment_method.lower()=="cash":
            monthly_cash_count+=1

print("\nTotal Earning:",revenue)
print("Total earning in current month:",monthly_revenue)

print("\nPayment used by customers:-")
print("Cash: ",cash_count,"times")
print("Card: ",card_count,"times")
print("UPI:  ",upi_count,"times")

print("\nPayment method used in current month by customers:-")
print("Cash: ",monthly_cash_count,"times")
print("Card: ",monthly_card_count,"times")
print("UPI:  ",monthly_upi_count,"times")