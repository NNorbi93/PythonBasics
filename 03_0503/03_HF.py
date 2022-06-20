import time
import datetime
import os
os.system("")


class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


productsDict = {
    "door": 30000,
    "window": 67000
}


def print_prod(products: dict):
    print(f"{Colors.BOLD}Product list:{Colors.RESET}")
    for index, (element, price) in enumerate(products.items()):
        print(f" {index}: {element}: {price}")  # \t - tabulator"""


def add(products: dict):
    timestamp = datetime.datetime.now()
    print("\n" + Colors.OKCYAN + "-" * 25 + " Adding/Modifying " + "-" * 25 + Colors.RESET)
    element: str = input(f"{Colors.OKBLUE}Add the name of the element: {Colors.RESET}")
    if element in products:
        print(f"{Colors.WARNING}{timestamp} - Element is already added!{Colors.RESET}")
        while True:
            timestamp = datetime.datetime.now()
            dec: str = str(input(f"{Colors.OKBLUE}Do you want to modify its price? (Y or N): {Colors.RESET}").upper())
            if dec == "Y":
                while True:
                    try:
                        price: int = int(input(f"{Colors.OKBLUE}Add the price of the element: {Colors.RESET}"))
                        products[element] = price  # Modify
                        print(f"{Colors.OKGREEN}{timestamp} - Element is modified!{Colors.RESET}")
                        break
                    except ValueError as e:
                        print(f"{Colors.FAIL}ValueError: {e}{Colors.RESET}")
                break
            elif dec == "N":
                print(f"{Colors.WARNING}{timestamp} - Element is NOT modified!{Colors.RESET}")
                break
            else:
                print(f"{Colors.FAIL}Please type Y or N{Colors.RESET}")
    else:
        while True:
            try:
                price: int = int(input(f"{Colors.OKBLUE}Add the price of the element: {Colors.RESET}"))
                products[element] = price  # Add
                print(f"{Colors.OKGREEN}{timestamp} - Element is added!{Colors.RESET}")
                break
            except ValueError as e:
                print(f"{Colors.FAIL}ValueError: {e}{Colors.RESET}")


def delete(products: dict):
    print("\n" + Colors.OKCYAN + "-" * 25 + " Deleting " + "-" * 25 + Colors.RESET)
    timestamp = datetime.datetime.now()
    while True:
        element: str = input("Add the name of the element: ")
        if element in products:
            productsDict.pop(element)  # Remove element
            print(f"{Colors.WARNING}{timestamp} - Element is deleted! \nList is updated!{Colors.RESET}")
            break
        else:
            print(f"{Colors.FAIL}The typed name doesn't exist!{Colors.RESET}")


def repo(products: dict):  # Infinite loop
    while True:
        timestamp = datetime.datetime.now()
        header: str = "\n" + Colors.OKBLUE + "-" * 25 + " Repository program " + "-" * 25 + Colors.RESET
        print(header)
        print_prod(products)
        option = int()
        print(f"\n{Colors.BOLD}Available options:{Colors.RESET} \n 1 - Add/Modify \n 2 - Delete \n 3 - Escape")
        try:
            option = int(input(f"\n{Colors.OKBLUE}Select an option (1 or 2 or 3): {Colors.RESET}"))
        except ValueError as e:
            print(f"{Colors.FAIL}ValueError: {e}{Colors.RESET}")
            continue
        if option == 1:
            add(products)
        elif option == 2:
            delete(products)
        elif option == 3:
            print(f"{Colors.WARNING}{timestamp} - You escaped from the program{Colors.RESET}")
            break  # Exit from infinite loop
        else:
            print(f"{Colors.FAIL}Not correct number! The typed input is not correct!{Colors.RESET}")
        time.sleep(1)


repo(productsDict)
