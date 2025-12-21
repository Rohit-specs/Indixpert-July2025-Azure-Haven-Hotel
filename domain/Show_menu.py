
import os
import json


class show_menu:
    def __init__(self):
        file_path=os.path.join("database","menu.json")
        with open(file_path,'r') as file:
            data=file.read()
        data=json.loads(data)
        # data=domain.file_reader(file_path,__name__)

        print("__________________________________________________________")
        print("|""              🏨 AZURE HAVEN HOTEL MENU 🏨              "+"|")
        print("__________________________________________________________")
        
        for key,dishes in data.items():
            key=key.title()
            print("|\t"+key+(49-len(key))*" "+"|")
            print("|\t"+len(key)*"_"+(49-len(key))*" "+"|")
            flag=1
            for dish in dishes:
                item=dish["item"]
                if "half plate" in dish and "full plate" in dish: 
                    spaces1=" "*(24-len(item))
                    spaces2=" "*(18-len(dish["half plate"]))
                    spaces3=" "*(13-len(dish["full plate"]))+"|"
                    if flag==1:
                        print("|"+" DISHES"+10*" "+"HALF PLATE PRICE"+4*" "+"FULL PLATE PRICE"+3*" "+"|")
                    print("| "+item+spaces1+dish["half plate"]+spaces2+dish["full plate"]+spaces3)
                    flag=0

                elif "price" in dish:
                    spaces1=" "*(28-len(item))
                    spaces2=" "*(27-len(dish["price"]))+"|"
                    if flag==1:
                        print("|"+" DISHES"+20*" "+"PRICE"+24*" "+"|")
                    print("| "+item+spaces1+dish["price"]+spaces2)
                    flag=0
            print("__________________________________________________________")

                            



            

