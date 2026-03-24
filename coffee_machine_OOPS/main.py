from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        break
    elif choice == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffee_machine.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_machine.make_coffee(drink)