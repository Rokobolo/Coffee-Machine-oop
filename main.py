from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def print_report():
    maker.report()
    coin_operator.report()


maker = CoffeeMaker()
coin_operator = MoneyMachine()
options = Menu()
is_on = True

while is_on:
    choice = input(f"What would you like? {options.get_items()}. ").lower()
    if choice == "report":
        print_report()
    elif choice == "off":
        is_on = False
    else:
        drink_choice = options.find_drink(choice)
        if maker.is_resource_sufficient(drink_choice) and coin_operator.make_payment(drink_choice.cost):
            maker.make_coffee(drink_choice)


