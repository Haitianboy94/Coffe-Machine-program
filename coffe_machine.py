import os
import time

water = 1000
milk = 300
coffee = 500
lst_of_coffee = ["espresso", "latte", "cappuccino"]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class CoffeeError(Exception):
    pass


class CoffeeTypeError(CoffeeError):
    def __init__(self, name_coffe):
        self.name_coffee = name_coffe
        super().__init__(f"Sorry! we don't have {name_coffe} available!")


stat_espresso = {
    "espresso":
        {"water": 50,
         "coffee": 18,
         "price": 2.50
         }
    }

stat_latte = {
    "latte":
        {"water": 200,
         "coffee": 24,
         "milk": 150,
         "price": 3.50
         }
    }

stat_cappuccino = {
    "cappuccino":
        {"water": 200,
         "coffee": 24,
         "milk": 150,
         "price": 4.50
         }
    }


def coffe_possible(the_coffee_name):
    if the_coffee_name == "latte":
        print("Check resources...")
        if water >= stat_latte["latte"]["water"] and coffee >= stat_latte["latte"]["coffee"] and milk >= stat_latte["latte"]["milk"]:
            print("We can make it!")
            return True
        print("Not enough resources!")
        return False
    elif the_coffee_name == "espresso":
        print("Check resources...")
        if water >= stat_espresso["espresso"]["water"] and coffee >= stat_espresso["espresso"]["coffee"]:
            print("We can make it!")
            return True
        print("Not enough resources!")
        return False
    elif the_coffee_name == "cappuccino":
        print("Check resources...")
        if water >= stat_cappuccino["cappuccino"]["water"] and coffee >= stat_cappuccino["cappuccino"]["coffee"] and milk >= stat_cappuccino["cappuccino"]["milk"]:
            print("We can make it!")
            return True
        print("Not enough resources!")
        return False


def repport():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")


def insert_coin() -> float:
    try:
        quarter = float(input("How many quarters?: "))
        dime = float(input("How many dimes?: "))
        nickel = float(input("How many nickels?: "))
        penny = float(input("How many pennies?: "))

        totalquater = quarter * 0.25
        totaldime = dime * 0.10
        totalnickle = nickel * 0.05
        totalpenny = penny * 0.01

        total = totalquater + totaldime + totalpenny + totalnickle
        return total

    except ValueError:
        print("You can only enter digits.")
        return 0.0


def coffeemaker(type_coff):
    global water, coffee, milk
    payment = 0.0
    while True:
        if type_coff == "espresso":
            espresso_price = stat_espresso["espresso"]["price"]
            print(f"You have to pay: ${espresso_price}")
            payment = insert_coin()
            print(f"You just pay ${round(payment, 3)}")
            if payment >= espresso_price:
                print(f"Here is you change: ${round(payment - espresso_price, 3)}")
                print("Enjoy Your coffee ☕")
                water = water - stat_espresso["espresso"]["water"]
                coffee = coffee - stat_espresso["espresso"]["coffee"]
                time.sleep(5)
                clear_screen()
                break
            elif payment < espresso_price:
                espresso_price = espresso_price - payment
                print(f"You need ${round(espresso_price, 3)} more")
        elif type_coff == "latte":
            latte_price = stat_latte["latte"]["price"]
            print(f"You have to pay: ${latte_price}")
            payment = insert_coin()
            print(f"You just pay ${round(payment, 3)}")
            if payment >= latte_price:
                print(f"Here is you change: ${round(payment - latte_price, 3)}")
                print("Enjoy Your coffee ☕")
                water = water - stat_latte["latte"]["water"]
                coffee = coffee - stat_latte["latte"]["coffee"]
                milk = milk - stat_latte["latte"]["milk"]
                time.sleep(5)
                clear_screen()
                break
            elif payment < latte_price:
                latte_price = latte_price - payment
                print(f"You need ${latte_price} more")
        elif type_coff == "cappuccino":
            cappu_price = stat_cappuccino["cappuccino"]["price"]
            print(f"You have to pay: ${cappu_price}")
            payment = insert_coin()
            print(f"You just pay ${round(payment, 3)}")
            if payment >= cappu_price:
                print(f"Here is you change: ${round(payment - cappu_price, 3)}")
                print("Enjoy Your coffee ☕")
                water = water - stat_cappuccino["cappuccino"]["water"]
                coffee = coffee - stat_cappuccino["cappuccino"]["coffee"]
                milk = milk - stat_cappuccino["cappuccino"]["milk"]
                time.sleep(5)
                clear_screen()
                break
            elif payment < cappu_price:
                cappu_price = cappu_price - payment
                print(f"You need ${round(cappu_price, 3)} more")


def start_machine():
    while True:
        try:
            print("Hello 🏭...☕")
            coffee_type = input("What would you like? "
                                "(espresso/latte/cappuccino):").lower()
            if coffee_type == "off":
                print("BYE")
                break
            elif coffee_type == "repport":
                repport()
            elif coffee_type not in lst_of_coffee:
                raise CoffeeTypeError(coffee_type)
            else:
                if coffe_possible(coffee_type):
                    coffeemaker(coffee_type)
                else:
                    print("Machine is on 'PAUSE' mode for maintenance!")
                    break
        except CoffeeTypeError as e:
            print(f"{e}")


if __name__ == "__main__":
    start_machine()
