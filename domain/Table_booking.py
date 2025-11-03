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
        
        self.booked_table_file=os.path.join('database','booked_table.json')
        self.menu_json=os.path.join("database","menu.json")
        self.order_json_file=os.path.join("database","customer_orders.json")
        self.payment_json_file=os.path.join("database","payment_file.json")
        self.discount_json_file=os.path.join("database","price_update.json")

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
        
        with open(self.discount_json_file,'r') as file:
            self.discount_data=json.loads(file.read())
        
        self.per_seat_cost=self.discount_data.get("seat cost")
        self.time_cost=self.discount_data.get("time cost")
        self.discount=self.discount_data.get("discount")
        self.discount_comment=self.discount_data.get("discount comment")
        self.total_no_of_seats=self.discount_data.get("no of seats")
        self.total_no_of_tables=self.discount_data.get("no of tables")


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
        total_tables=self.total_no_of_tables
        try:
            print(Fore.GREEN+"\n----------------TABLE_BOOKING----------------")
            self.customer_name=validation.valid_name("customer")
            print()
            while True:
                self.booked_table_date=validation.valid_date()
                print()
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

                if booking_start_time>=booking_end_time:
                    print(Fore.RED+"Please book table again.\nEnd time must be after start time")
                    return


                total_capacity=self.total_no_of_seats
                print(Fore.BLUE+"\nAviliable table on",self.booked_table_date,"from",self.booked_table_starttime,"to",self.booked_table_endtime)
                print()

                table_no=1
                while table_no<=total_tables:
                    space=3
                    remaining_seats=total_capacity

                    for booking in self.table_booking_data:
                        if booking.get("table no")==table_no and booking.get("table booking date")==self.booked_table_date:
                            old_start_parts=booking.get("booking start time")
                            old_end_parts=booking.get("booking end time")
                            old_start_parts=old_start_parts.split(":")
                            old_end_parts=old_end_parts.split(":")
                            old_start_min=int(old_start_parts[0])*60+int(old_start_parts[1])
                            old_end_min=int(old_end_parts[0])*60+int(old_end_parts[1])
                            if booking_start_time<old_end_min and old_start_min<booking_end_time:
                                remaining_seats-=booking.get("no of seats",0)
                    if (table_no-1)%10==0:
                        print()
                    if (table_no-1)<10:
                        space=4
                    if remaining_seats>0:
                        print("Table "+Fore.GREEN+str(table_no)+": "+str(remaining_seats),end=" "*space)
                    else:
                        print("Table "+Fore.RED+Fore.RED+str(table_no)+": FULL")
                    table_no+=1           

                print()
                print(Fore.BLUE+"\nIf the time is not sutiable you can:-")
                print("1. Write date and time again")
                print("2. Continue to book")
                print("3. Back to Staff menu")
                flag=False
                while True:
                    try:
                        choice=int(input("Enter your choice: "))
                        if choice==1:
                            flag=True
                            break
                        elif choice==2:
                            break
                        elif choice==3:
                            return
                        else:
                            print("Invalid number")
                    except Exception as error:
                        log_object=domain.log(error,__name__)
                        print("Invalid input,Please try again")
                if flag:
                    print()
                    continue

                print()
                self.table_no=validation.valid_table()

                remaining_seats=total_capacity

                for booking in self.table_booking_data:
                    if booking.get("table no")==self.table_no and booking.get("table booking date")==self.booked_table_date:
                        old_start=booking.get("booking start time")
                        old_end=booking.get("booking end time")

                        old_start_parts=old_start.split(":")
                        old_end_parts=old_end.split(":")

                        old_start_min=int(old_start_parts[0])*60+int(old_start_parts[1])
                        old_end_min=int(old_end_parts[0])*60+int(old_end_parts[1])

                        if booking_start_time< old_end_min and booking_end_time >old_start_min:
                            remaining_seats -=booking.get("no of seats", 0)

                if remaining_seats<=0:
                    print(Fore.RED+"Sorry, this table is already full for that time")
                    return
                else:
                    print(Fore.GREEN+"Table "+str(self.table_no)+" has "+str(remaining_seats)+" seats available")
                
                while True:
                    try:
                        self.no_of_seats=int(input("Enter number of seats to book (max "+str(self.total_no_of_seats)+"): "))
                        if 1<=self.no_of_seats<=remaining_seats:
                            break
                        else:
                            print(Fore.RED+"Only "+str(remaining_seats)+" seats available Please enter a valid number")
                    except Exception as error:
                        obj=domain.log(error, __name__)
                        print("Invalid input. Please enter a number")


                booked_seats=0
                for booking in self.table_booking_data:
                    if (booking.get("table no")==self.table_no and 
                        booking.get("table booking date")==self.booked_table_date):

                        old_start=booking.get("booking start time")
                        old_end=booking.get("booking end time")
                        old_start_parts=old_start.split(":")
                        old_end_parts=old_end.split(":")

                        old_start_min=int(old_start_parts[0])*60+int(old_start_parts[1])
                        old_end_min=int(old_end_parts[0])*60+int(old_end_parts[1])

                        if booking_start_time< old_end_min and booking_end_time >old_start_min:
                            booked_seats+=int(booking.get("no of seats", 0))


                if remaining_seats<=0:
                    print(Fore.RED+"Sorry, Table "+str(self.table_no)+" is fully booked for that time")
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
            log_obj=domain.log(error,__name__)
            print(Fore.RED+"Error Occurring while booking table")


    def show_booking_menu(self):

        while True:
            print(Fore.CYAN+"\n1.","View All Bookings")
            print(Fore.CYAN+"2.","View Todays Bookings")
            print(Fore.CYAN+"3.","Search Today Booking By Table Number")
            print(Fore.CYAN+"4.","Back To Staff Menu")
            try:
                choice=int(input("Enter a choice: "))
            except Exception as error:
                print("Invalid input.Please try again")
                log_obj=domain.log(error,__name__)
                continue
            if choice==1:
                self.show_all_booking()
            elif choice==2:
                self.show_todays_booking()
            elif choice==3:
                self.show_today_booking_on_table()
            elif choice==4:
                return
            else:
                print(str(choice)+" is not a valid choice")
            
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
            if booking_no==1:
                print("No one booked yet")
            
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(Fore.RED+"Error Occurred While loading Booking data")

    def show_todays_booking(self):
        try:
            print(Fore.GREEN+"\n---------------TODAY_BOOKINGS---------------")
            today_booking_count=1
            for booking in self.table_booking_data:
                if str(datetime.date.today())==booking.get("table booking date"):
                    print(Fore.RED+"\nBooking no=",today_booking_count)
                    print(Fore.BLUE+"ID:",booking.get("id"))
                    print("Customer name:",booking.get("customer name"))
                    print("Booked Table: ",booking.get("table no"))
                    print("Table Booking For Date: ",booking.get("table booking date"))
                    print("Start Time: ",booking.get("booking start time"))
                    print("End Time: ",booking.get("booking end time"))
                    print("Seats Booked By:",booking.get("no of seats"))
                    print("Table Booked By: ",booking.get("staff who booked"))
                    today_booking_count+=1
            if today_booking_count==1:
                print(Fore.RED,"No one booked yet")

        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(Fore.RED+"Error Occurred While loading Todays Booking data")


    def show_today_booking_on_table(self):
        try:
            table_no=validation.valid_table("table no")
            print(Fore.GREEN+"\n---------------TODAY_BOOKING_ON_THIS_TABLE---------------")
            today_booking_count=1
            for booking in self.table_booking_data:
                if (str(datetime.date.today())==booking.get("table booking date")) and (booking.get("table no")==table_no):
                    print(Fore.RED+"\nBooking no=",today_booking_count)
                    print(Fore.BLUE+"ID:",booking.get("id"))
                    print("Customer name:",booking.get("customer name"))
                    print("Booked Table: ",booking.get("table no"))
                    print("Table Booking For Date: ",booking.get("table booking date"))
                    print("Start Time: ",booking.get("booking start time"))
                    print("End Time: ",booking.get("booking end time"))
                    print("Seats Booked By:",booking.get("no of seats"))
                    print("Table Booked By: ",booking.get("staff who booked"))
                    today_booking_count+=1
            if today_booking_count==1:
                print(Fore.RED+"There is no booking for today")
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(Fore.RED+"Error Occurred While loading Booking data")

                        
    def take_order(self):
        try:
            print(Fore.GREEN+"\n---------------ORDER_FOOD---------------")
            if self.table_booking_data==[]:
                print("There are no bookings left")
                return
            else:
                id=input("Enter ID: ")
                
                for data in self.table_booking_data:
                    if data.get("id")==id:

                        for customer in self.table_booking_data:
                            if customer.get("id")==id:
                                date=customer.get("table booking date")
                                table_no=customer.get("table no")
                                if date!=str(datetime.date.today()):
                                    print(Fore.RED+"No booking for today\n")
                                    return

                                existing_order=None
                                for order in self.order_json:
                                    if order.get("id")==id:
                                        existing_order=order
                                        break
                            
                                food_items=[]
                                food_prices=[]
                                while True:
                                    order_data={
                                        "id": customer.get("id"),
                                        "customer name": customer.get("customer name"),
                                        "table no": table_no,
                                        "date":str(datetime.date.today()),
                                        "ordered items": food_items,
                                        "prices": food_prices
                                    }
                                    
                                    print(Fore.YELLOW+"ALL Category:-")
                                    for key,value in self.menu.items():
                                        print("\t-",key)
                                    print()

                                    category=input("Enter food category: ").lower()
                                    if category not in self.menu:
                                        print("Category not found")
                                        continue
                                    else:
                                        dishes=self.menu.get(category)
                                        if not dishes:
                                            print(Fore.RED+"No dishes available in this category. Choose another category.")
                                            continue
                                        print(Fore.YELLOW+"\nDishes in "+category+":-")
                                        for dish in dishes:
                                            item_name=dish.get("item")
                                            print("\t-",item_name," "*(20-len(item_name)))
                                        print()
                                            
                                    for key, value in self.menu.items():
                                        if category.lower()==key:
                                            sample=value[0]
                                            if "half plate" in sample and "full plate" in sample:
                                                item=input("Enter your dish name: ").title()
                                                for dish in value:
                                                    if dish["item"]==item:
                                                        print(Fore.CYAN+"\n1. for full plate")
                                                        print(Fore.CYAN+"2. for half plate")
                                                        choice=int(input("Enter your choice: "))
                                                        if choice==1:
                                                            food_items.append({item: "full plate"})
                                                            food_prices.append({item: dish.get("full plate")})
                                                        elif choice==2:
                                                            food_items.append({item: "half plate"})
                                                            food_prices.append({item: dish.get("half plate")})
                                                        else:
                                                            print(Fore.RED+"Invalid option!\nPlease try again")
                                                            continue
                                                        option=input("Do you wanna order more (yes/else): ")
                                                        if option.lower() !="yes":
                                                            if existing_order:
                                                                for item_data in food_items:
                                                                    existing_order["ordered items"].append(item_data)
                                                                for price_data in food_prices:
                                                                    existing_order["prices"].append(price_data)
                                                            else:
                                                                self.order_json.append(order_data)
                                                                
                                                            self.order_save()
                                                            return
                                            else:
                                                item=input("Enter your dish name: ").title()
                                                for dish in value:
                                                    if dish.get("item")==item:
                                                        food_items.append({item: "full plate"})
                                                        food_prices.append({item: dish.get("price")})
                                                        option=input("Do you wanna order more (yes/else): ")
                                                        if option.lower() !="yes":
                                                            if existing_order:
                                                                for item_data in food_items:
                                                                    existing_order["ordered items"].append(item_data)
                                                                for price_data in food_prices:
                                                                    existing_order["prices"].append(price_data)
                                                            else:
                                                                self.order_json.append(order_data)
                                                            self.order_save()
                                                            
                                                            return
                              
        except Exception as error:
            print(Fore.RED+"Error Occurring while taking orders")
            log_obj=domain.log(error,__name__)
    
    def show_order_menu(self):

        while True:
            print(Fore.CYAN+"\n1.","View All Orders")
            print(Fore.CYAN+"2.","View Todays Orders")
            print(Fore.CYAN+"3.","Search Today Orders By Table Number")
            print(Fore.CYAN+"4.","Back To Staff Menu")
            try:
                choice=int(input("Enter a choice: "))
            except Exception as error:
                print("Invalid input.Please try again")
                log_obj=domain.log(error,__name__)
                continue
            if choice==1:
                self.show_all_orders()
            elif choice==2:
                self.show_todays_order()
            elif choice==3:
                self.show_order_on_table()
            elif choice==4:
                return
            else:
                print(str(choice)+" is not a valid choice")


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
            if order_no==1:
                print(Fore.RED+"Nobody ordered yet")
            
                
        except Exception as error:
            print(Fore.RED+"Error occurred while loading all orders")
            log_obj=domain.log(error,__name__)

    def show_todays_order(self):
        try:
            print(Fore.GREEN+"\n--------------TODAY_ORDERS--------------")
            today_order_count=1
            for order in self.order_json:
                if str(datetime.date.today())==order.get("date"):
                    print(Fore.RED+"\nOrder no:",today_order_count)
                    print(Fore.CYAN+"ID     :",order.get("id"))
                    print("Customer name :",order.get("customer name"))
                    items=order.get("ordered items")
                    print("Ordered Items:")
                    for item in items:
                        for dish,price in item.items():
                            print("\t",dish," "*(20-(len(dish))),price)
                    today_order_count+=1
            if today_order_count==1:
                print(Fore.RED+"Nobody order yet")

        except Exception as error:
            print(Fore.RED+"Error occurred while loading todays orders")
            log_obj=domain.log(error,__name__)

    def show_order_on_table(self):
        try:
            table_no=validation.valid_table()
            print(Fore.GREEN+"\n--------------ALL_ORDER_IN_THIS_TABLE--------------")
            today_order_count=1
            for order in self.order_json:
                if (str(datetime.date.today())==order.get("date")) and (order.get("table no")==table_no):
                    print(Fore.RED+"\nOrder no:",today_order_count)
                    print(Fore.CYAN+"ID     :",order.get("id"))
                    print("Customer name :",order.get("customer name"))
                    items=order.get("ordered items")
                    print("Ordered Items:")
                    for item in items:
                        for dish,price in item.items():
                            print("\t",dish," "*(20-(len(dish))),price)
                    today_order_count+=1
            if today_order_count==1:
                print(Fore.RED+"There are no orders today on this table")

        except Exception as error:
            print(Fore.RED+"Error occurred while loading todays orders")
            log_obj=domain.log(error,__name__)



                    
    def payment(self):
        try:
            print(Fore.GREEN+"\n---------------PAYMENT---------------"+Fore.CYAN)
            id=input("Enter order id: ")
            for payment in self.payment_json:
                old_id=payment.get("order_id")
                if id==old_id:
                    print(Fore.RED+"You have already paid for meal")
                    return
            for data in self.order_json:
                if data.get("id")==id:
                    customer_name=data.get("customer name")
                    ordered_items=data.get("prices")
                    total=0
                    time=0
                    no_of_seats=0

                    for item in ordered_items:
                        for key, value in item.items():
                            total+=int(value)

                    for data in self.table_booking_data:
                        if data.get("id")==id:
                            time=data.get("booked time in min")
                            no_of_seats=data.get("no of seats")
                    discount=self.discount
                    discount_comment=self.discount_comment
                    seat_charge_per_person=self.per_seat_cost
                    seat_total=no_of_seats*seat_charge_per_person
                    time_charge=time*self.time_cost
                    gst=((seat_total+time_charge+total))*(2.5/100)
                    sub_total=total+time_charge+seat_total
                    total_bill=sub_total+(gst*2)

                    print(Fore.GREEN+"\n--------------PAYMENT OVERVIEW--------------")
                    print(Fore.CYAN+"ID                :",id)
                    print(Fore.CYAN+"Customer Name     :",customer_name)
                    print(Fore.CYAN+"Seat Charge("+str(seat_charge_per_person)+"ea.):",seat_total)
                    print(Fore.CYAN+"Booking duration  :","(",time,"x"+str(self.time_cost)+") =",time_charge)
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
                    if discount!=0:
                        total_discount=total_bill*(discount/100)
                        print("\t\tDiscount "+str(discount)+"%          : ",total_discount)
                        if discount_comment!=None:
                            print("\t\tDiscount Reason      : ",discount_comment)

                    print(Fore.GREEN+"\t\tTotal Bill           : ",round(total_bill-total_discount),"(~",total_bill-total_discount,")"+Fore.RED)

                    confirm=input(Fore.RED+"Do you want to proceed with payment? (yes/no): ").lower()

                    if confirm !="yes":
                        print(Fore.RED+"Payment cancelled")
                        return
                    while True:
                        print(Fore.CYAN+"\nSelect Payment Method")
                        print("1. Cash")
                        print("2. Card")
                        print("3. UPI")
                        try:
                            method_choice=int(input("Enter your choice : "))
                        except Exception as error:
                            print(method_choice,"is invalid")
                            log_obj=domain.log(error,__name__)
                            continue
                        if method_choice==1:
                            payment_method="Cash"
                            break
                        elif method_choice==2:
                            payment_method="Card"
                            break
                        elif method_choice==3:
                            payment_method="UPI"
                            break
                        else:
                            print(Fore.RED+"Invalid choice!")
                            continue

                    payment_details={
                        "order_id": id,
                        "customer_name": customer_name,
                        "payment_date":str(datetime.date.today()),
                        "ordered_items": ordered_items,
                        "discount": total_discount,
                        "amount without discount":total_bill,
                        "total_amount": total_bill-total_discount,
                        "payment_method": payment_method,
                        "booking duration(min)":time,
                        "no of seats":no_of_seats,
                        "seats charge total":seat_total
                    }

                    self.payment_json.append(payment_details)
                    self.payment_save()

                    print("\nPayment successful!")
                    print("Payment Method :",payment_method)
                    print(Fore.RED+"Total Paid     :",round(total_bill-total_discount))
                    print("-------------------------------")
                    return
        except Exception as error:
            print(Fore.RED+"Error Occurring while Paying bill")
            log_obj=domain.log(error,__name__)


    def get_invoice(self):
        try:
            for payment in self.payment_json:
                date=payment.get("payment_date")
            id=input("Enter Order ID: ")
            print(Fore.RED+"\n\n                 AZURE HAVEN HOTEL")
            print(Fore.RED+"                 Family Restaurant")
            print(Fore.RED+"        Palaspa Phata,Mumbai Pune Highway")
            print(Fore.RED+"             Near ONGC Colony,Panvel")
            print(Fore.YELLOW+"--------------------INVOICE--------------------")
            print("Payment date:",date)
            print(Fore.YELLOW+"-"*47)
            print(Fore.RED+"ITEMS                    Qty    Rate     Amount")
            print(Fore.YELLOW+"-"*47)
            for data in self.payment_json:
                if data.get("order_id")==id:
                    items=data.get("ordered_items")
                    time=data.get("booking duration(min)")
                    seats=data.get("no of seats")
                    seat_total=data.get("seats charge total")
                    discount=data.get("discount")
                    amount_without_discount=data.get("amount without discount")
                    total_amount=data.get("total_amount")

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
                            
                    time_price=time*self.time_cost
                    gst=((time_price+dish_total+seat_total)*(2.5/100))
                    sub_total=dish_total+(time_price)
                    # price_without_discount=Fore.RED,((time_price)+dish_total+seat_total+(gst*2))
                    
                    print(Fore.YELLOW+" "*27+"--------------------")
                    print(Fore.CYAN+" "*27+"Seat total:  ",seat_total)
                    print(Fore.CYAN+" "*27+"Time price:  ",time_price)
                    print(Fore.CYAN+" "*27+"Dish total:  ",dish_total)
                    print(Fore.CYAN+" "*27+"Sub Total :  ",sub_total)
                    print(Fore.CYAN+" "*27+"SGST(2.5%):  ",gst)
                    print(Fore.CYAN+" "*27+"CGST(2.5%):  ",gst)
                    if discount!=None:
                        print(Fore.CYAN+" "*27+"discount Rs:  ",discount)
                    print(Fore.YELLOW+" "*27+"--------------------")
                    print(Fore.CYAN+" "*26,"Food Total:  ",amount_without_discount)
                    if discount!=None:
                        print(Fore.CYAN+" "*27+"After dis.:  ",total_amount)
                    print(Fore.YELLOW+"-"*47)
                    print(Fore.RED+str(datetime.datetime.now().date())," "*13,"TOTAL:"," "*7,Fore.RED,round(amount_without_discount))
                    print(Fore.YELLOW+"-"*47)
                    print(Fore.RED+"time:",datetime.datetime.now().time(),end="   ")
                    print(Fore.RED+"Thank you",end="   ")
                    print(Fore.RED+"Visit Again")
                    return
            print(Fore.RED+"Id mismatched.\nPlease try again and check id")

        except Exception as error:
            print(Fore.RED+"Error occurring while generating invoice")
            log_obj=domain.log(error,__name__)


    def cancel_booking(self):
        try:
            print(Fore.GREEN+"\n--------------CANCEL BOOKING--------------")
            id=input("Enter id: ")
            for booking in self.table_booking_data:
                if booking.get("id")==id:
                    if self.payment_json:
                        for payment in self.payment_json:
                            if payment.get("order_id")==id:
                                print(Fore.GREEN+"order already completed")
                                return
                    
                    for order in self.order_json:
                        if order.get("id")==id:
                            print(Fore.RED+"Can't able to cancel booking after ordering food")
                            return

                    for key,value in booking.items():
                        print(key," :",value)

                    confirm=input(Fore.RED+"Enter yes to confirm cancellation: ")
                    if confirm.lower()!="yes":
                        print(Fore.RED+"Cancellation failed")
                        return
                    self.table_booking_data.remove(booking)
                    self.booking_save()
        
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(Fore.RED+"Error Occurring While Cancelling booking")
