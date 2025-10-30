from colorama import init,Fore
init(autoreset=True)
import domain
def valid_table(a="table number you want to book"):
    while True:
        try:
            print("Enter the",a,": ",end="")
            table_no=int(input())
        except Exception as error:
            obj=domain.log(error,__name__)
            print(Fore.RED+"invalid input Please try again\n")
            continue
        if table_no>50:
            print(Fore.RED+"Hotel have only 50 tables\n")
            continue
        elif table_no<=0:
            print(Fore.RED+"Invalid number\n")
            continue
        else:
            return table_no

