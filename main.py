from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


def order():
    drink = input(f"What drinks would you like to order? ({Menu().get_items()}): ")
    if drink == "OFF":
        print("Coffee machine has been turned off")
        return
    if drink.upper() == "REPORT":
        MoneyMachine().report()
        print("Ingredients:")
        CoffeeMaker().report()
        order()
    drink = Menu().find_drink(drink)
    if drink is None:
        order()
    if CoffeeMaker().is_resource_sufficient(drink):
        if MoneyMachine().make_payment(drink.cost):
            CoffeeMaker().make_coffee(drink)
    else:
        print("There are not enough resources for this coffee. Please choose another")
    order()
    
order()