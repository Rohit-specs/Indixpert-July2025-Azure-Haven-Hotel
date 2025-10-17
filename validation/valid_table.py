import domain
def valid_table(a="table number you want to book"):
    while True:
        try:
            print("Enter the",a,": ",end="")
            table_no=int(input())
        except Exception as error:
            obj=domain.log(error,__name__)
            print("invalid input Please try again")
            continue
        if table_no>50:
            print("Hotel have only 50 tables")
            continue
        elif table_no<=0:
            print("Invalid number")
            continue
        else:
            return table_no

