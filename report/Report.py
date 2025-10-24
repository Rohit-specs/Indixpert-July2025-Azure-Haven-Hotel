import json
import os
from domain import log
import datetime
booked_table_file=os.path.join("database","boked_table.json")
customer_order_file=os.path.join("database","customer_orders.json")
payment_file=os.path.join("database","payment_file.json")
with open(booked_table_file,'r') as data:
    try:
        table_booking_data=data.read()
    except Exception as error:
        obj=log(error,__name__)
        print("Error occurring while loading booked table json file.")
    try:
        table_booking_data=json.loads(table_booking_data)
    except Exception as error:
        obj=log(error,__name__)
        print("Please check if booked table is a valid json")


with open(customer_order_file,'r') as data:
    try:
        customer_order_data=data.read()
    except Exception as error:
        obj=log(error,__name__)
        print("Error occurring while loading booked table json file.")
    try:
        customer_order_data=json.loads(customer_order_data)
    except Exception as error:
        obj=log(error,__name__)
        print("Please check if booked table is a valid json")


with open(payment_file,'r') as data:
    try:
        payment_data=data.read()
    except Exception as error:
        obj=log(error,__name__)
        print("Error occurring while loading booked table json file.")
    try:
        payment_data=json.loads(payment_data)
    except Exception as error:
        obj=log(error,__name__)
        print("Please check if booked table is a valid json")
        
current_month_booking=0
number_of_booking=len(table_booking_data)
current_month=str(datetime.datetime.now().month)

for booking in table_booking_data:
    booking_duration=booking.get("booked time in min")
    
    average_booking_duration+=int(booking_duration)
    
    month_booking=booking.get("table booking date")
    modified_current_month="-"+current_month+"-"
    if modified_current_month in month_booking:
        current_month_booking+=1    
    
average_booking_duration=average_booking_duration/number_of_booking
print("No of booking",number_of_booking)
print("Current month booking:",current_month_booking)
print("Average booking duration:",average_booking_duration)

# nums = [1, 2, 3, 2, 4, 2, 5]
# print(max(set(nums), key=nums.count))
all_order_list=[]
for order in customer_order_data:
    data=order.get("ordered items")
    all_order_list.append(data)
print("Most ordered dish of all time",end=" ")
print(max(set(all_order_list),key=all_order_list.count))

revenue=0
upi_count=0
cash_count=0
card_count=0
for payment in payment_data:
    amount=payment.get("total_amount")
    revenue+=float(revenue)
    payment_method=payment.get("payment_method")
    if payment_method.lower()=="upi":
        upi_count+=1
    elif payment_method.lower()=="card":
        card_count+=1
    elif payment_method.lower()=="cash":
        cash_count+=1
    
print("Total Earning")

print("payment used by customer")
print("Cash: ",cash_count)
print("Card: ",card_count)
print("UPI:  ",upi_count)


    


    



