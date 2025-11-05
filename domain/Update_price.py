import json
import os
from colorama import init,Fore,Style
init(autoreset=True)
import domain


class update_pricing_structure():
    def __init__(self):
        
        self.price_update_file_path=os.path.join("database","price_update.json")
        with open(self.price_update_file_path,'r') as file:
            self.price_update_file=json.loads(file.read())

    def price_save(self):
        with open(self.price_update_file_path,'w') as file:
            file.write(json.dumps(self.price_update_file))
            print(Fore.GREEN+"Price updated")

    def update_price_menu(self):
        while True:
            print(Fore.GREEN+"\n------------Price & Discount Management Menu------------")
            print(Fore.CYAN+"1.","Change per seat cost")
            print(Fore.CYAN+"2.","Change time cost")
            print(Fore.CYAN+"3.","Apply discount and Can Change discount percentage")
            print(Fore.CYAN+"4.","Change no of seats")
            print(Fore.CYAN+"5.","Change no of table")
            print(Fore.CYAN+"6.","Back to Admin menu")
            while True:
                try:    
                    choice=int(input("\nEnter your choice: "))
                    break
                except Exception as error:
                    print("Invalid input. Please try again")
                    log_obj=domain.log(error,__name__)
            if choice==1:
                self.update_per_seat_cost()
            elif choice==2:
                self.update_time_duration_cost()
            elif choice==3:
                self.discount()
            elif choice==4:
                self.update_no_of_seats()
            elif choice==5:
                self.update_no_of_tables()
            elif choice==6:
                print(Fore.YELLOW+Style.DIM+"Exiting Price and Discount Management Menu")
                return
            else:
                print(Fore.RED+str(choice)+"is not a valid choice")
    
    def update_per_seat_cost(self):
        seat_price=str(self.price_update_file.get("seat cost"))
        print("\nEach seat cost: "+Fore.RED+seat_price)
        while True:
            try:
                new_seat_price=int(input("\nEnter price to update: "))
                if new_seat_price<0:
                    print(Fore.RED+"Price be must be positive number")
                    continue
                break
            except Exception as error:
                    print(Fore.RED+"Invalid input. Please try again with numbers")
                    log_obj=domain.log(error,__name__)
        print(Fore.RED+"Please confirm you want to change the price ",end="")
        print(seat_price+Fore.YELLOW+Style.DIM+" -->",new_seat_price)
        confirm=input("(yes/no):")
        if confirm!="yes":
            print(Fore.RED+"Update canceled")
            return
        self.price_update_file["seat cost"]=new_seat_price
        self.price_save()
        
    def update_time_duration_cost(self):
        current_time_cost=self.price_update_file.get("time cost")
        print("Time per minute cost: ",current_time_cost,"\n")
        while True:
            try:
                new_time_cost=int(input("\nEnter per minute cost to update: "))
                if new_time_cost<0:
                    print(Fore.RED+"Price be must be positive number")
                    continue
                break
            except Exception as error:
                    print(Fore.RED+"Invalid input. Please try again with numbers\n")
                    log_obj=domain.log(error,__name__)
        print(Fore.RED+"Please confirm you want to change the price ",end="")
        print(str(current_time_cost)+Fore.YELLOW+Style.DIM+" -->",str(new_time_cost))
        confirm=input("(yes/no):").lower()
        if confirm!="yes":
            print(Fore.RED+"Update canceled")
            return
        self.price_update_file["time cost"]=new_time_cost
        self.price_save()

    def discount(self):
        while True:
            try:
                discount=int(input("Enter what percentage of discount you want to give: "))
                if discount<0:
                    print(Fore.RED+"discount percentage be must be positive number")
                    continue
                elif discount>100:
                    print(Fore.RED+"discount perentage must be smaller than 100")
                    continue
            except Exception as error:
                    print(Fore.RED+"Invalid input. Please try again with numbers\n")
                    log_obj=domain.log(error,__name__)
            if discount==100:
                print(Fore.RED+"You entered 100%\nAll orders will be free")
                confirm=input(Fore.RED+"Are you sure about discount percentage(yes/no)").lower()
                if confirm!="yes":
                    continue
            break
        print(Fore.GREEN+Style.DIM+"Will you want to add comment on discount")
        print(Fore.CYAN+"1.","yes")
        print(Fore.CYAN+"2.","no")
        while True:
            try:    
                choice=int(input("Enter your choice: "))
                break
            except Exception as error:
                print(Fore.RED+"Invalid input. Please try again")
                log_obj=domain.log(error,__name__)
        if choice==1:
            while True:
                comment=input("Enter on which occation you are giving discount: ").strip()
                if len(comment)<6:
                    print(Fore.RED+"Comment contain atleast 7 character")
                    continue
                elif len(comment)>=40:
                    print(Fore.RED+"Comment can contain maximum 40 characters")
                    continue
                break

        self.price_update_file["discount"]=discount
        if choice==1:
            self.price_update_file["discount comment"]=comment
        else :
            self.price_update_file["discount comment"]=None
        self.price_save()
                

    def update_no_of_seats(self):
        current_no_of_seats=self.price_update_file.get("no of seats")
        print("Total no of seats currently: ",current_no_of_seats,"\n")
        while True:
            try:
                new_no_of_seats=int(input("\nEnter no of seats to update: "))
                if new_no_of_seats<0:
                    print(Fore.RED+"No of seats should be greater than 0")
                    continue
                elif new_no_of_seats>12:
                    print(Fore.RED+"Seats of a table is maximum 12")
                    continue
                break
            except Exception as error:
                    print(Fore.RED+"Invalid input. Please try again with numbers\n")
                    log_obj=domain.log(error,__name__)
        print(Fore.RED+"Please confirm you want to change the no of seats ",end="")
        print(str(current_no_of_seats)+Fore.YELLOW+Style.DIM+" -->",str(new_no_of_seats))
        confirm=input("(yes/no):").lower()
        if confirm!="yes":
            print(Fore.RED+"Update canceled")
            return
        self.price_update_file["no of seats"]=new_no_of_seats
        self.price_save()
    
    
    def update_no_of_tables(self):
        current_no_of_tables=self.price_update_file.get("no of tables")
        print("Total no of tables currently: ",current_no_of_tables,"\n")
        while True:
            try:
                new_no_of_tables=int(input("\nEnter no of tables to update: "))
                if new_no_of_tables<8:
                    print(Fore.RED+"Number of tables should be greater than 8")
                    continue
                if new_no_of_tables>99:
                    print(Fore.RED+"This software is perfectly work if no of table is below 100")
                    continue
                break
            except Exception as error:
                    print(Fore.RED+"Invalid input. Please try again with numbers\n")
                    log_obj=domain.log(error,__name__)
        print(Fore.RED+"Please confirm you want to change the no of tables ",end="")
        print(str(current_no_of_tables)+Fore.YELLOW+Style.DIM+" -->",str(new_no_of_tables))
        confirm=input("(yes/no):").lower()
        if confirm!="yes":
            print(Fore.RED+"Update canceled")
            return
        self.price_update_file["no of tables"]=new_no_of_tables
        self.price_save()



