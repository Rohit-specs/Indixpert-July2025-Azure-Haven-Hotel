import json
import os
import validation
import uuid
import datetime
import domain
from colorama import init,Fore,Back,Style
init(autoreset=True)

class tablebooking:
    def __init__(self):
        
        self.booked_table_file = os.path.join('database','booked_table.json')
        self.menu_json=os.path.join("database","menu.json")
        self.order_json_file=os.path.join("database","customer_orders.json")
        self.payment_json_file=os.path.join("database","payment_file.json")

        if not os.path.exists(self.booked_table_file):
            with open(self.booked_table_file, 'w') as f:
                self.table_booking_data=[]
                self.table_booking_data=json.dumps(self.table_booking_data)
                f.write(self.table_booking_data)
        
        with open(self.booked_table_file,'r') as file:
            data=file.read()
            if data:
                self.table_booking_data=json.loads(data)
            else:
                self.table_booking_data=[]

        with open(self.menu_json,'r') as file:
            self.menu=file.read()
            self.menu=json.loads(self.menu)
            
        if not os.path.exists(self.order_json_file):
            with open(self.order_json_file, 'w') as f:
                self.order_json=[]
                self.order_json=json.dumps(self.order_json)
                f.write(self.order_json)
        
        with open(self.order_json_file,'r') as file:
            data=file.read()
            if data:
                self.order_json=json.loads(data)
            else:
                self.order_json=[]

        if not os.path.exists(self.payment_json_file):
            with open(self.payment_json_file,'w') as file:
                self.payment_json=[]
                self.payment_json=json.dumps(self.payment_json)
                file.write(self.payment_json)
        
        with open(self.payment_json_file,'r') as file:
            data=file.read()
            if data:
                self.payment_json=json.loads(data)
            else:
                self.payment_json=[]


    def booking_save(self):
        with open(self.booked_table_file,'w') as file:
            self.table_booking_data=json.dumps(self.table_booking_data,indent=2)
            file.write(self.table_booking_data)
            print("Booking success")
    
    def order_save(self):
        with open(self.order_json_file,'w') as data:
            self.order_json=json.dumps(self.order_json,indent=2)
            data.write(self.order_json)
            print("Order save")

    def payment_save(self):
        with open(self.payment_json_file,'w') as file:
            self.payment_json=json.dumps(self.payment_json,indent=2)
            file.write(self.payment_json)
            print("Payment data save")
            
    def book_table(self,staff_booked_table):
        try:
            print(Fore.GREEN+"\n----------------TABLE_BOOKING----------------")
            
            self.customer_name=validation.valid_name("customer")
            self.booked_table_date=validation.valid_date()
            self.booked_table_starttime=validation.valid_time("starting")
            self.booked_table_endtime=validation.valid_time("end")
            self.staff_booked_table=staff_booked_table
            id=str(uuid.uuid4())[:6]
            
            time=0
            list_start_time=[]
            list_end_time=[]
            order_start=self.booked_table_starttime
            order_start=order_start.split(":")
            order_end=self.booked_table_endtime
            order_end=order_end.split(":")
            for i in order_start:
                data=int(i)
                list_start_time.append(data)
            for i in order_end:
                data=int(i)
                list_end_time.append(data)
                
            booking_start_time=(list_start_time[0]*60+list_start_time[1])
            booking_end_time=(list_end_time[0]*60+list_end_time[1])
            time=(booking_end_time-booking_start_time)
            
            if booking_start_time>booking_end_time:
                print("Please book table again.\n You have enter wrong time")
                return
            
            booked_tables=[]
            for booking in self.table_booking_data:
                
                if booking.get("table booking date")==self.booked_table_date:
                    old_start=booking.get("booking start time")
                    old_end=booking.get("booking end time")
                    
                    old_start_parts = old_start.split(":")
                    old_end_parts = old_end.split(":")

                    old_start_hour = int(old_start_parts[0])
                    old_start_minute = int(old_start_parts[1])
                    old_end_hour = int(old_end_parts[0])
                    old_end_minute = int(old_end_parts[1])

                    old_start_minutes = (old_start_hour * 60) + old_start_minute
                    old_end_minutes = (old_end_hour * 60) + old_end_minute
                    if booking_start_time < old_end_minutes and booking_end_time > old_start_minutes:
                        booked_tables.append(booking.get("table no"))
                        
                        
                        
            avialable_table=[]
            for i in range(1,51):
                if i not in booked_tables:
                    avialable_table.append(i)
            print(Fore.BLUE+"\nAviliable table on",self.booked_table_date,"from",self.booked_table_starttime,"to",self.booked_table_endtime)
            if len(avialable_table)>0:
                # print(Fore.CYAN,avialable_table)
                i=1
                for table in avialable_table:
                    print(table,end=" ")
                    if i%10==0:
                        print()
                    i+=1
            else:
                print(Fore.RED+"No table avialiable at this time.")
                    
            
            print()
            self.table_no=validation.valid_table()
            
            
            
            while True:
                try:
                    self.no_of_seats = int(input("Enter number of seats to book (max 6): "))
                    if 1 <= self.no_of_seats <= 6:
                        break
                    else:
                        print(Fore.RED+"Seats must be between 1 and 6")
                except Exception as error:
                    obj=domain.log(error,__name__)
                    print("Invalid input. Please enter a number.")
            
            
            
            for booking in self.table_booking_data:
               
                if booking.get("table no")==self.table_no:
                        if booking.get("table booking date")==self.booked_table_date:
                            list_old_start_time=[]
                            list_old_end_time=[]
                            list_new_start_time=[]
                            list_new_end_time=[]
                            old_order_start=booking.get("booking start time")
                            old_order_start=old_order_start.split(":")
                            old_order_end=booking.get("booking end time")
                            old_order_end=old_order_end.split(":")
                            new_order_start=self.booked_table_starttime
                            new_order_start=new_order_start.split(":")
                            new_order_end=self.booked_table_endtime
                            new_order_end=new_order_end.split(":")
                            for i in old_order_start:
                                data=int(i)
                                list_old_start_time.append(data)
                            for i in old_order_end:
                                data=int(i)
                                list_old_end_time.append(data)
                            for i in new_order_start:
                                data=int(i)
                                list_new_start_time.append(data)
                            for i in new_order_end:
                                data=int(i)
                                list_new_end_time.append(data)

                            old_start_minutes = list_old_start_time[0]*60 + list_old_start_time[1]
                            old_end_minutes = list_old_end_time[0]*60+ list_old_end_time[1]
                            new_start_minutes = list_new_start_time[0]*60 + list_new_start_time[1]
                            new_end_minutes = list_new_end_time[0]*60 + list_new_end_time[1]
                            if new_start_minutes < old_end_minutes and new_end_minutes > old_start_minutes:
                                print(Fore.RED+"This table is already booked For same time you want!")
                                return
            
            modified_data={
                "id":id,
                "table no":self.table_no,
                "table booking date":self.booked_table_date,
                "booking start time":self.booked_table_starttime,
                "booking end time":self.booked_table_endtime,
                "staff who booked":self.staff_booked_table,
                "customer name":self.customer_name,
                "no of seats":self.no_of_seats,
                "booked time in min":time
                }
            self.table_booking_data.append(modified_data)
            self.booking_save()
            
            return
        except Exception as error:
            obj=domain.log(error,__name__)
            print(Fore.RED+"Error Occurring while booking table")


    def show_all_booking(self):
        try:
            print(Fore.GREEN+"\n-----------------ALL_BOOKINGS-----------------")
            booking_no=1
            for booking in self.table_booking_data:
                print(Fore.RED+"\nBooking no=",booking_no)
                print(Fore.BLUE+"ID:",booking.get("id"))
                print("Customer name:",booking.get("customer name"))
                print("Booked Table: ",booking.get("table no"))
                print("Table Booking For Date: ",booking.get("table booking date"))
                print("Start Time: ",booking.get("booking start time"))
                print("End Time: ",booking.get("booking end time"))
                print("Seats Booked By:",booking.get("no of seats"))
                print("Table Booked By: ",booking.get("staff who booked"))  
                booking_no+=1
            
        except Exception as error:
            obj=domain.log(error,__name__)
            print(Fore.RED+"Error Occurred While loading Booking data")
    
                        
    def take_order(self):
        try:
            print(Fore.GREEN+"\n---------------ORDER_FOOD---------------"+Fore.CYAN)
            if self.table_booking_data == []:
                print("There are no bookings left")
                return
            else:
                id=input("Enter ID: ")
                for data in self.table_booking_data:
                    if data.get("id")==id:

                        for customer in self.table_booking_data:
                            if customer.get("id")==id:
                                date=customer.get("table booking date")#new lines
                                if date!=str(datetime.date.today()):#new lines
                                    print("Not booked for today\n")#new lines
                                    return#new lines
                            
                                food_items = []
                                food_prices = []
                                while True:
                                    order_data = {
                                        "id": customer.get("id"),
                                        "customer name": customer.get("customer name"),
                                        "date":str(datetime.datetime.now()),#here are some changes
                                        "ordered items": food_items,
                                        "prices": food_prices
                                    }
                                    # print(self.menu.key())
                                    print(Fore.YELLOW+"ALL Category:-")
                                    for key,value in self.menu.items():
                                        print("\t-",key)#here and in next print 
                                    print()
                                    category = input("Enter food category: ").lower()
                                    if category not in self.menu:
                                        print("Category not found")
                                        continue
                                    else:
                                        dishes=self.menu.get(category)
                                        print(Fore.YELLOW+"\nDishes in "+category+":-")
                                        for dish in dishes:
                                            item_name=dish.get("item")
                                            # half_price=str(dish.get("half plate"))
                                            # full_price=str(dish.get("full plate"))
                                            print("\t-",item_name," "*(20-len(item_name)))#some changes
                                            # print(half_price," "*(8-len(half_price)),full_price)
                                        print()
                                            
                                    for key, value in self.menu.items():
                                        if category.lower() == key:
                                            sample = value[0]
                                            if "half plate" in sample and "full plate" in sample:
                                                item = input("Enter your dish name: ").title()
                                                for dish in value:
                                                    if dish["item"] == item:
                                                        print(Fore.CYAN+"\n1. for full plate")
                                                        print(Fore.CYAN+"2. for half plate")
                                                        choice = int(input("Enter your choice: "))
                                                        if choice == 1:
                                                            food_items.append({item: "full plate"})
                                                            food_prices.append({item: dish.get("full plate")})
                                                        elif choice == 2:
                                                            food_items.append({item: "half plate"})
                                                            food_prices.append({item: dish.get("half plate")})
                                                        else:
                                                            print(Fore.RED+"Invalid option!\nPlease try again")
                                                            continue
                                                        option = input("Do you wanna order more (yes/else): ")
                                                        if option.lower() != "yes":
                                                            self.order_json.append(order_data)
                                                            self.order_save()
                                                            return
                                            else:
                                                item = input("Enter your dish name: ").title()
                                                for dish in value:
                                                    if dish.get("item") == item:
                                                        food_items.append({item: "full plate"})
                                                        food_prices.append({item: dish.get("price")})
                                                        option = input("Do you wanna order more (yes/else): ")
                                                        if option.lower() != "yes":
                                                            self.order_json.append(order_data)
                                                            self.order_save()
                                                            
                                                            return
                              
        except Exception as error:
            print(Fore.RED+"Error Occurring while taking orders")
            obj=domain.log(error,__name__)


    def show_all_orders(self):
        try:
            print(Fore.GREEN+"\n-------------ALL_ORDERS-------------")
            order_no=1
            for order in self.order_json:
                print(Fore.RED+"\nOrder no:",order_no)
                print(Fore.CYAN+"ID     :",order.get("id"))
                print("Customer name :",order.get("customer name"))
                items=order.get("ordered items")
                print("Ordered Items:")
                for item in items:
                    for dish,price in item.items():
                        print("\t",dish," "*(20-(len(dish))),price)
                order_no+=1
            
                
        except Exception as error:
            print(Fore.RED+"Error occurred while loading all orders")
            obj=domain.log(error,__name__)


                    
    def payment(self):
        try:
            print(Fore.GREEN+"\n---------------PAYMENT---------------"+Fore.CYAN)
            id = input("Enter order id: ")
            for payment in self.payment_json:#new lines
                old_id=payment.get("order_id")#new lines
                if id==old_id:#new lines
                    print("You have already paid for meal")#new lines
                    return#new lines
            for data in self.order_json:
                if data.get("id") == id:
                    customer_name = data.get("customer name")
                    ordered_items = data.get("prices")
                    total = 0
                    time=0
                    no_of_seats=0

                    for item in ordered_items:
                        for key, value in item.items():
                            total+=int(value)

                    for data in self.table_booking_data:
                        if data.get("id")==id:
                            time=data.get("booked time in min")
                            no_of_seats=data.get("no of seats")

                    seat_charge_per_person=50
                    seat_total=no_of_seats*seat_charge_per_person
                    time_charge=time*4
                    gst=((seat_total+time_charge+total))*(2.5/100)
                    sub_total=total+time_charge+seat_total
                    total_bill=sub_total+(gst*2)

                    print(Fore.GREEN+"\n--------------PAYMENT OVERVIEW--------------")
                    print(Fore.CYAN+"ID                :",id)
                    print(Fore.CYAN+"Customer Name     :",customer_name)
                    print(Fore.CYAN+"Seat Charge(50ea.):",seat_total)
                    print(Fore.CYAN+"Booking duration  :","(",time,"x 4"+")=",time_charge)
                    print(Fore.CYAN+"Booking time Price:",time_charge)
                    print(Fore.YELLOW+"\t\tDishes"+" "*16+"Price")
                    for item in ordered_items:
                        for key,value in item.items():
                            space=" "*(21-len(key))
                            print("\t\t"+key+space+"{"+value+"}"+"x1")

                    print("\n\t\tDishes total         : ",total)
                    print("\t\tSubtotal             : ",sub_total)
                    print("\t\tCGST(2.5%)           : ",gst)
                    print("\t\tCGST(2.5%)           : ",gst)
                    print("\t\tTotal GST            : ",gst+gst)
                    print(Fore.GREEN+"\t\tTotal Bill           : ",round(total_bill),"(~",total_bill,")"+Fore.RED)

                    confirm = input(Fore.RED+"Do you want to proceed with payment? (yes/no): ").lower()

                    if confirm != "yes":
                        print(Fore.RED+"Payment cancelled")
                        return
                    while True:
                        print(Fore.CYAN+"\nSelect Payment Method")
                        print("1. Cash")
                        print("2. Card")
                        print("3. UPI")
                        try:
                            method_choice = int(input("Enter your choice : "))
                        except Exception as error:
                            print(method_choice,"is invalid")
                            obj=domain.log(error,__name__)
                            continue
                        if method_choice == 1:
                            payment_method = "Cash"
                            break
                        elif method_choice == 2:
                            payment_method = "Card"
                            break
                        elif method_choice == 3:
                            payment_method = "UPI"
                            break
                        else:
                            print("Invalid choice!")
                            continue

                    payment_details = {
                        "order_id": id,
                        "customer_name": customer_name,
                        "payment_date":str(datetime.date.today()),#added date in dictionary
                        "ordered_items": ordered_items,
                        "total_amount": total_bill,
                        "payment_method": payment_method,
                        "booking duration(min)":time,
                        "no of seats":no_of_seats,
                        "seats charge total":seat_total
                    }

                    self.payment_json.append(payment_details)
                    self.payment_save()

                    print("\nPayment successful!")
                    print("Payment Method :",payment_method)
                    print(Fore.RED+"Total Paid     :",total_bill)
                    print("-------------------------------")
                    return
        except Exception as error:
            print(Fore.RED+"Error Occurring while Paying bill")
            obj=domain.log(error,__name__)


    def get_invoice(self):
        try:
            for payment in self.payment_json:#new changes
                date=payment.get("payment_date")#new changes
            id=input("Enter Order ID: ")
            print(Fore.RED+"\n\n                 AZURE HAVEN HOTEL")
            print(Fore.RED+"                 Family Restaurant")
            print(Fore.RED+"        Palaspa Phata,Mumbai Pune Highway")
            print(Fore.RED+"             Near ONGC Colony,Panvel")
            print(Fore.YELLOW+"--------------------INVOICE--------------------")
            print("Payment date:",date)#modified date
            print(Fore.YELLOW+"-"*47)
            print(Fore.RED+"ITEMS                    Qty    Rate     Amount")
            print(Fore.YELLOW+"-"*47)
            for data in self.payment_json:
                if data.get("order_id")==id:
                    items=data.get("ordered_items")
                    time=data.get("booking duration(min)")
                    seats=data.get("no of seats")
                    seat_total=data.get("seats charge total")
                    dish_total=0
                    for item in items:
                        for key,value in item.items():
                            str_key=str(key)
                            str_value=str(value)
                            space1=" "*(24-len(str_key))
                            space2=" "*3
                            space3=" "*(9-len(str_value))
                            print(key,space1,"1",space2,value,space3,value)
                            dish_total+=float(value)
                            
                    time_price=time*4
                    gst=((time_price+dish_total+seat_total)*(2.5/100))
                    sub_total=dish_total+(time_price)
                    print(Fore.YELLOW+" "*27+"--------------------")
                    print(Fore.CYAN+" "*27+"Seat total:  ",seat_total)
                    print(Fore.CYAN+" "*27+"Time price:  ",time_price)
                    print(Fore.CYAN+" "*27+"Dish total:  ",dish_total)
                    print(Fore.CYAN+" "*27+"Sub Total :  ",sub_total)
                    print(Fore.CYAN+" "*27+"SGST(2.5%):  ",gst)
                    print(Fore.CYAN+" "*27+"CGST(2.5%):  ",gst)
                    print(Fore.YELLOW+" "*27+"--------------------")
                    print(" "*26,"Food Total:  ",Fore.RED,((time_price)+dish_total+seat_total+(gst*2)))
                    print(Fore.YELLOW+"-"*47)
                    print(Fore.RED+str(datetime.datetime.now().date())," "*13,"TOTAL:"," "*7,Fore.RED,round(time_price+dish_total+seat_total+(gst*2)))
                    print(Fore.YELLOW+"-"*47)
                    print(Fore.RED+"time:",datetime.datetime.now().time(),end="   ")
                    print(Fore.RED+"Thank you",end="   ")
                    print(Fore.RED+"Visit Again")
                    return
                
        except Exception as error:
            print(Fore.RED+"Error occurring while generating invoice")
            obj=domain.log(error,__name__)


    def cancel_booking(self):
        try:
            print(Fore.GREEN+"\n--------------CANCEL BOOKING--------------")
            id=input("Enter id: ")
            for booking in self.table_booking_data:
                if booking.get("id")==id:
                    if self.payment_json:
                        for payment in self.payment_json:
                            if payment.get("order_id")==id:
                                print("order already completed")
                                return


                    for key,value in booking.items():
                        print(key," :",value)

                    confirm=input(Fore.RED+"Enter yes to confirm cancellation: ")
                    if confirm.lower()!="yes":
                        print("Cancellation failed")
                        return
                    self.table_booking_data.remove(booking)
                    self.booking_save()
        
        except Exception as error:
            obj=domain.log(error,__name__)
            print(Fore.RED+"Error Occurring While Cancelling booking")
