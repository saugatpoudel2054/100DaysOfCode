MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

ESPRESSO = 'espresso'
CAPPUCCINO = 'cappuccino'
LATTE = 'latte'


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# TODO 1. Print report consisting of remaining water, milk and coffee
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# TODO 3: Check resource sufficient?
def resource_check(user_choice):
    if user_choice == ESPRESSO:
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return 1
        else:
            return 0
    elif user_choice == LATTE:
        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
            return 1
        else:
            return 0
    elif user_choice == CAPPUCCINO:
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
            return 1
        else:
            return 0
    elif user_choice == 'report':
        print_report()


# TODO: Accept coins
def accept_coins():
    print('Please insert coins.')
    q = int(input('How many quarters: '))
    d = int(input('How many dimes: '))
    n = int(input('How many nickels: '))
    p = int(input('How many pennies: '))
    return q, d, n, p


# TODO 4: Process coins
def process_coins(p, n, d, q):
    return (p*1 + n*5 + d*10 + q*25) / 100


# TODO 5: Check if user money is enough
def check_money(user_choice, user_money):
    if user_choice == ESPRESSO:
        if user_money >= MENU[ESPRESSO]['cost']:
            return user_money - MENU[ESPRESSO]['cost']
        else:
            print('Insufficient money')
            return -1
    elif user_choice == LATTE:
        if user_money >= MENU[LATTE]['cost']:
            return user_money - MENU[LATTE]['cost']
        else:
            print('Insufficient money')
            return -1
    elif user_choice == CAPPUCCINO:
        if user_money >= MENU[CAPPUCCINO]['cost']:
            return user_money - MENU[CAPPUCCINO]['cost']
        else:
            print('Insufficient money')
            return -1


# TODO reduce resources
def reduce_resource(user_choice):
    if user_choice == ESPRESSO:
        resources['water'] -= 50
        resources['coffee'] -= 18
        resources['money'] += MENU[ESPRESSO]['cost']
    elif user_choice == LATTE:
        resources['water'] -= 200
        resources['coffee'] -= 24
        resources['milk'] -= 150
        resources['money'] += MENU[LATTE]['cost']
    elif user_choice == CAPPUCCINO:
        resources['water'] -= 250
        resources['coffee'] -= 24
        resources['milk'] -= 100
        resources['money'] += MENU[CAPPUCCINO]['cost']


# TODO 2. Ask for user input

while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'report':
        print_report()
        continue
    elif choice == 'off':
        print("Turning off machine...")
        break
    else:
        if resource_check(choice) == 1:
            q, d, n, p = accept_coins()
            money = process_coins(p, n, d, q)
            print(money)
            change = check_money(choice, money)
            if change != -1:
                print(f'Here is your ${change} in change')
                reduce_resource(choice)
                print_report()
        else:
            print('Insufficient resources.')













