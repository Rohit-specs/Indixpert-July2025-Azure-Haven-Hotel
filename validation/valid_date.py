import domain
import datetime
from colorama import init,Fore
init(autoreset=True)

def valid_date():
    current_year=datetime.datetime.now().year
    current_month=datetime.datetime.now().month
    current_day=datetime.datetime.now().day
    date=""
    while True:
        print("1. Booking for today")
        print("2. ELSE")
        try:
            choice=int(input("Enter your choice: "))
        except Exception as error:
            print(Fore.RED+"Please enter a number\n")
            log_obj=domain.log(error,__name__)
            continue
        break
    if choice==1:
        date=str(datetime.date.today())
        return date
    elif choice==2:
        while True:
            try:
                year=int(input("Enter year: "))
            except Exception as error:
                print(Fore.RED+"Please enter a valid year\n")
                log_obj=domain.log(error,__name__)
                continue
            if year<current_year+1:
                print("You can't accept that long booking")
                continue
            if year<current_year or len(str(year))!=4:
                print(Fore.RED+f"Please enter a valid year. you have entered {year}\n")
                continue
            else:
                break
        date=str(year)+"-"
        while True:
            try:
                month=int(input("Enter month: "))
            except Exception as error:
                print(Fore.RED+"Please enter a month in numbers\n")
                log_obj=domain.log(error,__name__)
                continue
            if month<10:
                month="0"+str(month)
            if month>12 or month<current_month:
                print(Fore.RED+f"You have entered {month}\nPlease enter a valid month\n")
                continue
            else:
                break
        date=date+str(month)+"-"
        while True:
            try:
                day=int(input("Enter day: "))
            except Exception as error:
                print(Fore.RED+"Please enter day in number\n")
                log_obj=domain.log(error,__name__)
                continue
            if day<10:
                day="0"+str(day)
            if day>31 or day<current_day:
                print(Fore.RED+f"you have entered {day} Please enter a valid day\n")
                continue
            else:
                break
        date=date+str(day)
        return date
    else:
        print(Fore.RED+"please enter a valid option\n")
    
