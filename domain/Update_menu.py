
import domain
import json



class update_menu:
    def __init__(self, path):
        self.path=path
        try:
            with open(self.path,'r') as data:
                self.menu=json.loads(data.read())
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print(error)

    def save(self):
        try:
            with open(self.path,'w') as data:
                self.menu=json.dumps(self.menu)
                data.write(self.menu)
            print("Changes saved to file")
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print("Faliled to save menu to file")

    def delete_dish(self):
        try:
            print("\n--------------DELETE DISH--------------")
            category=input("Enter the dish category: ").lower()
            dish_name=input("Enter the dish name to delete: ").title()

            if category in self.menu:
                dishes=self.menu[category]
                for dish in dishes:
                    if dish['item'].lower()==dish_name.lower():
                        dishes.remove(dish)
                        print("Dish deleted")
                        self.save()
                        return
                print("Dish not found")
            else:
                print("Category not found")
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print("Something went wrong while deleting the dishes")

    def add_dish(self):
        try:
            print("\n--------------ADD DISH--------------")
            category=input("Enter the category to add the dish to: ")
            if category not in self.menu:
                print("Category not found")
                return
            item=input("Enter dish name: ").title()
            if len(self.menu[category]) > 0:
                sample_dish=self.menu[category][0]
            else:
                sample_dish={}
            if "half plate" in sample_dish and "full plate" in sample_dish:
                while True:
                    try:
                        half_price=int(input("Enter half plate price: "))
                        if half_price<10:
                            print("The minimun Half plate price you can set for any item is 10")
                            continue
                        break
                    except Exception as error:
                        log_obj=domain.log(error,__name__)
                        print("invalid Half plate price. please enter a number")
                
                while True:
                    try:
                        full_price=int(input("Enter full plate price: "))
                        if full_price<=half_price:
                            print("Full plate price should be greater than Half plate price")
                            continue
                        break
                    except Exception as error:
                        log_obj=domain.log(error,__name__)
                        print("invalid Half plate price. please enter a number")
                
                self.menu[category].append(
                    {
                    "item": item,
                    "half plate": str(half_price),
                    "full plate": str(full_price)
                    })
            elif "price" in sample_dish or not sample_dish:
                while True:
                    try:
                        price=int(input("Enter price: "))
                        if price<10:
                            price("Price must be greater than and equal to 10")
                            continue
                        break
                    except Exception as error:
                        log_obj=domain.log(error,__name__)
                        print("Invalid price.Please enter a number")
                self.menu[category].append({
                    "item": item,
                    "price": str(price)
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
                        while True:
                            try:
                                half_price=int(input("Enter half plate price: "))
                                if half_price<10:
                                    print("The minimun Half plate price you can set for any item is 10")
                                    continue
                                break
                            except Exception as error:
                                log_obj=domain.log(error,__name__)
                                print("invalid half price. please enter a number")
                
                        while True:
                            try:
                                full_price=int(input("Enter full plate price: "))
                                if full_price<=half_price:
                                    print("Full plate price should be greater than Half plate price")
                                    continue
                                break
                            except Exception as error:
                                log_obj=domain.log(error,__name__)
                                print("invalid half price. please enter a number")
                                self.menu[category].append(
                                    {
                                    "item": item,
                                    "half plate": str(half_price),
                                    "full plate": str(full_price)
                            })
                    elif choice==2:
                        while True:
                            try:
                                price=int(input("Enter price: "))
                                if price<10:
                                    price("Price must be greater than and equal to 10")
                                    continue
                                break
                            except Exception as error:
                                log_obj=domain.log(error,__name__)
                                print("Invalid price.Please enter a number")

                        self.menu[category].append({
                            "item": item,
                            "price": str(price)})
                    else:
                        print("invalid choice\nPlease try again")
                        continue
                    break
            print("Dish added")
            self.save()
        except Exception as error:
            domain.log(error,__name__)
            print("An error while adding the dish")

    def add_category(self):
        try:
            print("\n--------------ADD CATEGORY--------------")
            category=input("Enter new category name: ")
            if category in self.menu:
                print("Category already exists")
                return
            self.menu[category]=[]
            print("Category"+str(category)+"added")
            self.save()
        except Exception as error:
            domain.log(error,__name__)
            print("Error while adding a new category")

    def del_category(self):
        try:
            print("\n--------------DELETE CATEGORY--------------")
            category=input("Enter category name:")
            if category in self.menu:
                del self.menu[category]
                self.save()
                print("Category deleted successfully")
            else:
                print("Category not found")
        except Exception as error:
            log_obj=domain.log(error,__name__)
            print("Error occurred while deleting the category")
                    

    def update_price(self):
        try:
            print("\n--------------UPDATE PRICE--------------")
            category=input("Enter the category of the dish: ")
            category=category.lower()
            dish_name=input("Enter the dish name to update: ")
            dish_name=dish_name.title()

            if category in self.menu:
                for dish in self.menu[category]:
                    if dish['item'].lower()==dish_name.lower():
                        if "half plate" in dish and "full plate" in dish:
                            while True:
                                try:
                                    half_price=int(input("Enter new half plate price: "))
                                    if half_price<10:
                                        print("Half plate price must equal to or greater than 10")
                                        continue
                                    break
                                except Exception as error:
                                    log_obj=domain.log(error,__name__)
                                    print("invalid price,please try again")
                                    
                            while True:
                                try:
                                    full_price=int(input("Enter new full plate price: "))
                                    if half_price>=full_price:
                                        print("Full price must be greater than half plate price")
                                    break
                                except Exception as error:
                                    log_obj=domain.log(error,__name__)
                                    print("invalid price,please try again")
                                
                            
                            dish["half plate"]=str(half_price)
                            dish["full plate"]=str(full_price)
                        elif "price" in dish:
                            while True:
                                try:
                                    price=int(input("Enter new price: "))
                                    break
                                except ValueError as error:
                                    domain.log(error, __name__)
                                    print("Invalid price, please try again.")
                                dish["price"]=str(price)
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
            log_obj=domain.log(error,__name__)
            print("An error occurred while updating the price")
            
            
            