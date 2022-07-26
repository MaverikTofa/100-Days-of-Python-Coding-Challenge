"""
Create a program to run a Coffee Machine and process resources and money
"""

from project_resources import machine

menu = machine.MENU
starting_resources = machine.resources
starting_resources["money"] = 0


def not_available(ordr, res):
    """check availability of drink water,milk and coffee
    input the drink name
    return None if it is available else sorry msg"""
    not_sufficient = []
    for key, value in menu[ordr]["ingredients"].items():
        if value > res[key]:
            not_sufficient.append(key)
    message = f"Sorry there is not enough: {', '.join(not_sufficient)}"
    return message if not_sufficient else None


def resource_manage(ordr, res):
    for key, value in menu[ordr]["ingredients"].items():
        res[key] -= menu[ordr]["ingredients"][key]
    return None


def process_money(qrt=0, dim=0, nik=0, pns=0):
    return sum([qrt * .25, dim * .1, nik * .05, pns * .01])


def handle_money(ordr, paid):
    if menu[ordr]["cost"] > paid:
        return False
    elif menu[ordr]["cost"] == paid:
        resources["money"] += menu[ordr]["cost"]
        return True
    else:
        resources["money"] += menu[ordr]["cost"]
        return f'{paid - menu[ordr]["cost"]:.2f}'


def reporting(res):
    for key, value in res.items():
        if key == "money":
            print(f"{key}: ${value}")
        elif key == "coffee":
            print(f"{key}: {value}g")
        else:
            print(f"{key}: {value}ml")


while True:

    resources = starting_resources

    order = input("What would you like? (espresso,latte,cappuccino): ").lower()

    if order == "off":
        break
    elif order == "report":
        reporting(resources)
    elif order in ['espresso', 'latte', 'cappuccino']:
        availability = not_available(order, resources)
        if availability:
            print(availability)
        else:
            print("Please insert coins.")
            qrts = int(input("How many quarters?: "))
            dims = int(input("How many dimes?: "))
            niks = int(input("How many nickles?: "))
            pnss = int(input("How many pennies?: "))
            money = process_money(qrt=qrts, dim=dims, nik=niks, pns=pnss)

            is_money_enough = handle_money(order, money)
            if is_money_enough == False:
                print(f"Sorry that's not enough money. {money} refunded")
            else:
                if type(is_money_enough) == str:
                    resource_manage(order, resources)
                    print(f"Here is ${is_money_enough} dollars in change\n")
                    print(f"Here is your {order}. Enjoy!")
                else:
                    resource_manage(order, resources)
                    print(f"Here is your {order}. Enjoy!")
    else:
        print("Please choose a valid drink (espresso,latte,cappuccino)")
