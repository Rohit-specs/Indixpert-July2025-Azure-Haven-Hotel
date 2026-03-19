import domain
import datetime


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
            print("Please enter a number\n")
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
                print("Please enter a valid year\n")
                log_obj=domain.log(error,__name__)
                continue
            if not year<(current_year+1):
                print(current_year)
                print("You can't accept that long booking")
                continue
            if  year<current_year or len(str(year))!=4:
                print(f"Please enter a valid year. you have entered {year}\n")
                continue
            else:
                break
        date=str(year)+"-"
        while True:
            try:
                month=int(input("Enter month: "))
            except Exception as error:
                print("Please enter a month in numbers\n")
                log_obj=domain.log(error,__name__)
                continue
            if month>12 or month<current_month:
                print(f"You have entered {month}\nPlease enter a valid month\n")
                continue
            else:
                if month<10:
                    month="0"+str(month)
                break
        date=date+str(month)+"-"
        while True:
            try:
                day=int(input("Enter day: "))
            except Exception as error:
                print("Please enter day in number\n")
                log_obj=domain.log(error,__name__)
                continue
            if day>31 or day<current_day:
                print(f"you have entered {day} Please enter a valid day\n")
                continue
            else:
                if day<10:
                    day="0"+str(day)
                break
        date=date+str(day)
        return date
    else:
        print("please enter a valid option\n")
    
