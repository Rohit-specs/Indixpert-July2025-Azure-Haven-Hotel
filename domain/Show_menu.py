from colorama import init,Fore,Back,Style
import os
import json


file_path=os.path.join("database","menu.json")
class show_menu:
    def __init__(self):
        with open(file_path,'r') as file:
            data=file.read()
        data=json.loads(data)
        print(Fore.RED+"__________________________________________________________")
        print("|              🏨 AZURE HAVEN HOTEL MENU 🏨              |")
        print("__________________________________________________________")
        
        for key,dishes in data.items():
            key=key.title()
            print(Fore.GREEN+"|\t"+Fore.CYAN+key+(49-len(key))*" "+Fore.GREEN+"|")
            print("|\t"+Fore.YELLOW+len(key)*"_"+(49-len(key))*" "+Fore.GREEN+"|")
            flag=1
            for dish in dishes:
                item=dish["item"]
                if "half plate" in dish and "full plate" in dish: 
                    spaces1=" "*(22-len(item))
                    spaces2=" "*(12-len(dish["half plate"]))
                    spaces3=" "*(16-len(dish["full plate"]))+"|"
                    if flag==1:
                        print("| DISHES",8*" ","HALF PLATE PRICE",2*" ","FULL PLATE PRICE",1*" ","|")
                    print("|",Fore.YELLOW+item,spaces1,Style.RESET_ALL+dish["half plate"],spaces2,dish["full plate"],Fore.GREEN+spaces3)
                    flag=0

                elif "price" in dish:
                    spaces1=" "*(22-len(item))
                    spaces2=" "*(30-len(dish["price"]))+"|"
                    if flag==1:
                        print("| DISHES",14*" ","PRICE",26*" ","|")
                    print("|",Fore.YELLOW+item,spaces1,Style.RESET_ALL+dish["price"],Fore.GREEN+spaces2)
                    flag=0
            print("__________________________________________________________"+Style.RESET_ALL)

                            



            

