from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
        continue
    elif choice == 'off':
        print("Turning off machine...")
        break
    else:
        item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
