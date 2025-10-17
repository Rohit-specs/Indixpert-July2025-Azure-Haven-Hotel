from colorama import init,Fore,Style,Back
import domain
import json


class update_menu:
    def __init__(self, path):
        self.path = path
        try:
            with open(path,'r') as data:
                self.menu = json.loads(data.read())
        except Exception as error:
            obj=domain.log(error,__name__)
            print(error)

    def save(self):
        try:
            with open(self.path,'w') as data:
                self.menu=json.dumps(self.menu,indent=1)
                data.write(self.menu)
            print("Changes saved to file")
        except Exception as error:
            obj=domain.log(error,__name__)
            print("Faliled to save menu to file")

    def delete_dish(self):
        try:
            print(Fore.GREEN+"\n--------------DELETE DISH--------------"+Fore.YELLOW)
            category = input("Enter the dish category: ")
            dish_name = input("Enter the dish name to delete: ")

            if category in self.menu:
                dishes = self.menu[category]
                for dish in dishes:
                    if dish['item'].lower() == dish_name.lower():
                        dishes.remove(dish)
                        print("Dish deleted")
                        self.save()
                        return
                print("Dish not found")
            else:
                print("Category not found")
        except Exception as error:
            domain.log(error,__name__)
            print("Something went wrong while deleting the dishes")

    def add_dish(self):
        try:
            print(Fore.GREEN+"\n--------------ADD DISH--------------"+Fore.YELLOW)
            category = input("Enter the category to add the dish to: ")
            if category not in self.menu:
                print("Category not found")
                return
            item = input("Enter dish name: ")
            if len(self.menu[category]) > 0:
                sample_dish = self.menu[category][0]
            else:
                sample_dish = {}
            if "half plate" in sample_dish and "full plate" in sample_dish:
                half_price = input("Enter half plate price: ")
                full_price = input("Enter full plate price: ")
                
                self.menu[category].append(
                    {
                    "item": item,
                    "half plate": half_price,
                    "full plate": full_price
                    })
            elif "price" in sample_dish or not sample_dish:
                price = input("Enter price: ")
                self.menu[category].append({
                    "item": item,
                    "price": price
                    })
            else:
                while True:
                    print("Unknown pricing structure")
                    print("1. Create Half plate price and full plate price column")
                    print("2. Create only Price column")
                    try:
                        choice=int(input("Enter your choice: "))
                    except Exception as error:
                        print("Invalid choice! Please enter a number")
                        domain.log(error,__name__)
                        continue
                    if choice==1:
                        half_price = input("Enter half plate price: ")
                        full_price = input("Enter full plate price: ")
                        self.menu[category].append(
                            {
                            "item": item,
                            "half plate": half_price,
                            "full plate": full_price
                            })
                    elif choice==2:
                        price = input("Enter price: ")
                        self.menu[category].append({
                            "item": item,
                            "price": price})
                    break
            print("Dish added")
            self.save()
        except Exception as error:
            domain.log(error,__name__)
            print("An error while adding the dish")

    def add_category(self):
        try:
            print(Fore.GREEN+"\n--------------ADD CATEGORY--------------"+Fore.YELLOW)
            category = input("Enter new category name: ")
            if category in self.menu:
                print("Category already exists")
                return
            self.menu[category] = []
            print("Category",category,"added")
            self.save()
        except Exception as error:
            domain.log(error,__name__)
            print("Error while adding a new category")

    def del_category(self):
        try:
            print(Fore.GREEN+"\n--------------DELETE CATEGORY--------------"+Fore.YELLOW)
            category=input("Enter category name:")
            if category in self.menu:
                del self.menu[category]
                self.save()
                print("Category deleted successfully")
            else:
                print("Category not found")
        except Exception as error:
            obj=domain.log(error,__name__)
            print("Error occurred while deleting the category")
                    

    def update_price(self):
        try:
            print(Fore.GREEN+"\n--------------UPDATE PRICE--------------"+Fore.YELLOW)
            category = input("Enter the category of the dish: ")
            dish_name = input("Enter the dish name to update: ")

            if category in self.menu:
                for dish in self.menu[category]:
                    if dish['item'].lower() == dish_name.lower():
                        if "half plate" in dish and "full plate" in dish:
                            half_price = input("Enter new half plate price: ")
                            full_price = input("Enter new full plate price: ")
                            dish["half plate"] = half_price
                            dish["full plate"] = full_price
                        elif "price" in dish:
                            price = input("Enter new price: ")
                            dish["price"] = price
                        else:
                            print("Unknown pricing structure")
                            return
                        print("Price updated")
                        self.save()
                        return
                print("Dish not found")
            else:
                print("Category not found")
        except Exception as error:
            obj=domain.log(error,__name__)
            print("An error occurred while updating the price")
            
            
            