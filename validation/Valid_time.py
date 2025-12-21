

import domain
import datetime
def valid_time(option="starting"):
    current_hour=datetime.datetime.now().hour
    current_minute=datetime.datetime.now().minute
    while True:
        try:
            print("Enter",option,"hour: ",end="")
            hour=int(input())
            if hour>=22:
                print("22:00 is closing time of our Resturant\nYou can book till 21:59\n")
                continue
            if hour<7:
                print("7:00 is opening time of our Resturant\nYou can book after 07:00\n")
                continue
            if hour<current_hour:
                print(hour,"is incorrect\nWe can't travel back in time\n")
                continue
        except Exception as error:
            obj=domain.log(error,__name__)
            print("Please enter only hour in numbers\n")
            continue
        break
    time=str(hour)+":"
    while True:
        try:
            print("Enter",option,"minute: ",end="")
            minute=int(input())
            if hour==current_hour and current_minute>minute:
                print("That time has already passed\n")
                continue
            elif minute<0 and minute>60:
                print("Minute must be between 0 and 60\n")
                continue
        except Exception as error:
            obj=domain.log(error,__name__)
            print("Please enter only minute in numbers\n")
            continue
        break
    time=time+str(minute)
    return time


    