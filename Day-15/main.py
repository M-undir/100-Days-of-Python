from information import MENU, resources

profit = 0


def has_sufficient_resources(drink_ingredients):
    for i in resources:
        if drink_ingredients[i] > resources[i]:
            print("We don't have enough of {i}")
            return False
        return True


def pay_coins():
    print("Please insert coins.")
    total = float(input("How many quarters?: "))*0.25
    total += float(input("How many dimes?: "))*0.1
    total += float(input("How many nickels?: "))*0.05
    total += float(input("How many pennies?: "))*0.01
    return total


def process_coins(money_received, drink_cost):
    global profit
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    profit += drink_cost
    change = "{:.2f}".format(money_received - drink_cost)
    print(f"Here's ${change} in change")
    return True


def coffee_maker(drink_ingredients):
    for ingredients in drink_ingredients:
        resources[ingredients] -= drink_ingredients[ingredients]
    print(f"Here's your {choice}!")


# has_sufficient_resources(drink["ingredients"])

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        break
    elif choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\nMoney: ${profit}")
    else:
        drink = MENU[choice]
        if has_sufficient_resources(drink["ingredients"]):
            payment = pay_coins()
            if process_coins(payment, drink["cost"]):
                coffee_maker(drink["ingredients"])
