from colorama import init,Fore
init(autoreset=True)
import os
from domain import log
def valid_table(a="table number you want to book"):
    json_file_path=os.path.join("database","price_update.json")
    with open(json_file_path,'r') as file:
        price_data=json.loads(file.read())
        Total_table=price_data.get("no of tables")
    while True:
        try:
            print("Enter the",a,": ",end="")
            table_no=int(input())
        except Exception as error:
            log_obj=log(error,__name__)
            print(Fore.RED+"invalid input Please try again\n")
            continue
        if table_no>Total_table:
            print(Fore.RED+"Hotel have only 50 tables\n")
            continue
        elif table_no<=0:
            print(Fore.RED+"Invalid number\n")
            continue
        else:
            return table_no

