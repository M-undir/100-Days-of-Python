from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ordering = True
menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()


while ordering:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        break
    elif choice == 'report':
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                # print('yes')
                coffee_maker.make_coffee(drink)
