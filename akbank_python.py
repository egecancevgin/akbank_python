import csv
import datetime


class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Classic Pizza"
        self.cost = 8.99


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 10.99


class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turkish Pizza"
        self.cost = 12.99


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olive(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Olive"
        self.cost = 0.99


class Mushroom(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mushroom"
        self.cost = 0.79


class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Goat Cheese"
        self.cost = 1.29


class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Meat"
        self.cost = 1.49


class Onion(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Onion"
        self.cost = 0.69


class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Corn"
        self.cost = 0.59


def main():
    # Read menu from file
    with open('Menu.txt', 'r') as file:
        menu = file.read()

    # Print menu
    print(menu)

    # Get pizza and sauce selections
    pizza = input("Please select a pizza: ")
    sauce = input("Please select a sauce: ")

    # Create pizza object
    if pizza == "1":
        selected_pizza = ClassicPizza()
    elif pizza == "2":
        selected_pizza = MargheritaPizza()
    elif pizza == "3":
        selected_pizza = TurkishPizza()
    else:
        selected_pizza = Pizza()

    # Add sauce to pizza
    if sauce == "11":
        selected_pizza = Olive(selected_pizza)
    elif sauce == "12":
        selected_pizza = Mushroom(selected_pizza)
    elif sauce == "13":
        selected_pizza = GoatCheese(selected_pizza)
    elif sauce == "14":
        selected_pizza = Meat(selected_pizza)
    elif sauce == "15":
        selected_pizza = Onion(selected_pizza)
    elif sauce == "16":
        selected_pizza = Corn(selected_pizza)

    # Get total cost of pizza
    total_cost = selected_pizza.get_cost()

    # Get user information
    name = input("Please enter your name: ")
    id_num = input("Please enter your ID number: ")
    card_pin = input("Please enter your credit card PIN: ")

    # Create order object
    now = datetime.datetime.now()
    order_time = now.strftime("%Y-%m-%d %H:%M:%S")
    order = {'user': name, 'id': id_num, 'pizza': pizza.get_description(),
             'sauce': sauce.get_description(), 'time': order_time}

    # Write order to csv file
    with open('Orders_Database.csv', mode='a', newline='') as order_file:
        fieldnames = ['user', 'id', 'pizza', 'sauce', 'time']
    writer = csv.DictWriter(order_file, fieldnames=fieldnames)

    writer.writerow(order)

    print("Order complete! Thank you for your purchase.")
