from colorama import init,Fore
init(autoreset=True)
import domain
import datetime
def valid_time(option="starting"):
    current_hour=datetime.datetime.now().hour
    current_minute=datetime.datetime.now().minute
    while True:
        try:
            print(f"Enter {option} hour: ",end="")
            hour=int(input())
            if hour>=22:
                print(Fore.RED+"22:00 is closing time of our Resturant\nYou can book till 21:59\n")
                continue
            if hour<7:
                print(Fore.RED+"7:00 is opening time of our Resturant\nYou can book after 07:00\n")
                continue
            if hour<current_hour:
                print(Fore.RED+hour+"is incorrect\nWe can't travel back in time\n")
                continue
        except Exception as error:
            obj=domain.log(error,__name__)
            print(Fore.RED+"Please enter only hour in numbers\n")
            continue
        break
    time=str(hour)+":"
    while True:
        try:
            print(f"Enter {option} minute: ",end="")
            minute=int(input())
            if hour==current_hour and current_minute>minute:
                print(Fore.RED+"That time has already passed\n")
                continue
            elif minute<0 and minute>60:
                print(Fore.RED+"Minute must be between 0 and 60\n")
                continue
        except Exception as error:
            obj=domain.log(error,__name__)
            print(Fore.RED+"Please enter only minute in numbers\n")
            continue
        break
    time=time+str(minute)
    return time


    