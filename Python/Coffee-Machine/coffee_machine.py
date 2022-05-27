from menu import menu, resources


def coffee_calculation(cost):
    if cost == 1.5:
        coffee = 18
        return coffee
    elif cost == 2.5:
        coffee = 24
        return coffee
    elif cost == 3.0:
        coffee = 24
        return coffee


def water_calculation(cost):
    if cost == 1.5:
        water = 50
        return water
    elif cost == 2.5:
        water = 200
        return water
    elif cost == 3.0:
        water = 250
        return water


def milk_calculation(cost):
    if cost == 1.5:
        pass
    elif cost == 2.5:
        milk = 150
        return milk
    elif cost == 3.0:
        milk = 100
        return milk


def total_cost(user_input):
    if user_input == "report":
        pass
    else:
        cost = menu[user_input]["cost"]
        return cost


remain_water = resources["water"]
remain_milk = resources["milk"]
remain_coffee = resources["coffee"]

while remain_water > 0 and remain_milk > 0 and remain_coffee > 0:

    print("What would you like? (espresso/latte/cappuccino) : ", end="")
    user_input = input()
    if user_input == "report":
        print("Water: ", remain_water)
        print("Milk: ", remain_milk)
        print("Coffee: ", remain_coffee)

    else:
        print("how many quarters?: ", end="")
        quarters = .25 * float(input())
        print("how many dime?: ", end="")
        dime = .10 * float(input())
        print("how many nickles?: ", end="")
        nickles = .05 * float(input())
        print("how many pennies?: ", end="")
        pennies = .01 * float(input())
        money = quarters
        cost = total_cost(user_input)

        if money >= cost:
            remain_coffee = remain_coffee - coffee_calculation(cost)
            remain_water = remain_water - water_calculation(cost)
            if milk_calculation(cost) is None:
                pass
            else:
                remain_milk = remain_milk - milk_calculation(cost)

            print(f"Here is ${money-cost} in change")
            print(f"Here is your {user_input} Enjoy.")

        elif cost > money:
            print("Sorry that's not enough money. Money refunded.")
