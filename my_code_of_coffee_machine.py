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

PROFIT = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report_printing(resources_left):
    """Takes the available resources and prints those in required format"""
    water = resources_left["water"]
    milk = resources_left["milk"]
    coffee = resources_left["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${PROFIT}")


def are_resources_sufficient(required_ingredients, resources_left):
    """Takes the required ingredients for ordered drink and resources left
     and returns True if resources_left are enough or False if resources_left are insufficient"""
    for item in required_ingredients:
        if required_ingredients[item] > resources_left[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_payment():
    """asks the user to make the payment and returns the total amount paid"""
    print("Please insert coins.")
    total_payment = int(input("how many quarters?: ")) * 0.25
    total_payment += int(input("how many dimes?: ")) * 0.10
    total_payment += int(input("how many nickles?: ")) * 0.05
    total_payment += int(input("how many pennies?: ")) * 0.01
    return total_payment


def is_payment_sufficient(amount_paid, cost_of_drink):
    """Takes the amount paid and the cost of the drink and compares them and
    returns True if paid amount is sufficient to buy the ordered drink or else returns False"""
    if amount_paid < cost_of_drink:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif amount_paid > cost_of_drink:
        change = round((amount_paid - cost_of_drink), 2)
        print(f"Here is ${change} in change.")
    return True


def make_coffee(drink_name, ingredients):
    """takes the drink name and its ingredients and
    deducts the amounts of ingredients required from available resources """
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


machine_is_ON = True

# TODO: 4. make the process of prompting the user in 'TODO 1' repeatable
while machine_is_ON:

    # TODO: 1. Prompt the user "What would you like? (espresso/latte/cappuccino): "
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. make the machine to switch off if user gives the input 'off'
    if user_choice == "off":
        machine_is_ON = False

    # TODO: 3. Print the report of available resources if user asks for it
    elif user_choice == "report":
        report_printing(resources)

    else:
        drink = MENU[user_choice]

        # TODO: 5. make some functionality to Check if the required
        #  amounts of ingredients for drink ordered, are available in the resources
        if are_resources_sufficient(drink["ingredients"], resources):
            print(f"The cost of {user_choice} is ${drink['cost']} ")

            # TODO: 6. if resources available are sufficient then make some functionality
            #  to ask the user to insert the coins and return the total payment
            total_amount_paid = make_payment()

            # TODO: 7. make some functionality to check if the payment is enough to buy the ordered drink,
            #  if it is not sufficient then give the feedback to the user and refund their payment and
            #  if it is sufficient then add it to the profit of the machine
            if is_payment_sufficient(total_amount_paid, drink["cost"]):
                PROFIT += drink["cost"]

                # TODO: 8. if user payment is sufficient then make some functionality
                #  to make the coffee which deducts the amount of required ingredients
                #  for the ordered drink from available amounts of resources and give the user their order
                make_coffee(user_choice, drink["ingredients"])
