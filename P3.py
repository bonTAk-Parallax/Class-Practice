class Lunch:
    def __init__(self):
        print("")
        print("Select an item from the menu: press 1 for momo, 2 for pizza and 3 for Ham-Burger.")
        self.menu = input("Enter your order:\t")
        print(f"You ordered item number-{self.menu} from the menu.")

    def display(self, val):
        if val==0:
            return print("Select a valid dish from the available menu.")           
        print(f"Price for item number-{self.menu} is: {val}")

    def menu_price(self):
        if int(self.menu) == 1:
            val = 12.00
        elif int(self.menu) == 2:
            val = 15.00
        elif int(self.menu) == 3:
            val = 20.00
        else:
            val = 0
        self.display(val)

break_lunch = Lunch()
break_lunch.menu_price()
    


    

