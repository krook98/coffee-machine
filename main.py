import menu

is_on = True


def process_coins():
    total = int(input("How many pennies?: ")) * 0.01
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many quarters?: ")) * 0.25
    return total


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        menu.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


def are_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > menu.resources[item]:
            print(f"Sorry, there's no enough {item}")
            return False
        return True


def print_report():
    for i in menu.resources:
        key, value = i, menu.resources[i]
        print(f"{key}: {value}")
    print(f"Money: {menu.profit}")


def transaction_complete(money_received, get_cost):
    if money_received >= get_cost:
        change = round(money_received - get_cost, 2)
        print(f"You payed {money_received}. Here is your ${change} change")
        menu.profit += get_cost
        return True
    else:
        print(f"There is not enough many, sorry. Here is your money: ${money_received}")
        return False


while is_on:
    answer = input("What would you like? (espresso/latte/cappuccino)")
    if answer == 'report':
        print(f"Water: {menu.resources['water']} ml")
        print(f"Milk: {menu.resources['milk']} ml")
        print(f"Coffee: {menu.resources['coffee']} ml")
        print(f"Money: ${menu.profit} ")
    elif answer == 'off':
        is_on = False
        print("Goodbye")
    else:
        drink = menu.MENU[answer]
        print(f"The drink cost is ${drink['cost']}")
        if are_resources_sufficient(drink['ingredients']):
            pay = process_coins()
            if transaction_complete(pay, drink['cost']):
                make_coffee(answer, drink['ingredients'])













