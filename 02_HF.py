import time

productsDict = {
    "door": 30000,
    "window": 67000
}


def print_prod(products: dict):
    print(f"Product list:")
    for index, (element, price) in enumerate(products.items()):
        print(f"\t{index}: {element}: {price}")  # \t - tabulator"""


def add(element: str, price: int):
    productsDict[element] = price  # Modify/add
    print("Element is added/modified!")


def delete(element: str, products: dict):
    if element in products:
        productsDict.pop(element)  # Remove element
        print("Element is deleted!")
    else:
        print("The typed name doesn't exist!")


def repo(products: dict):  # Infinite loop
    while True:
        print("\n" + "-" * 25 + " Repository program " + "-" * 25)
        print_prod(products)
        option = int()
        element = str()
        price = int()
        print("\nAvailable options: \n 1 - Add/Modify \n 2 - Delete \n 3 - Escape")
        option = input("\nSelect an option: ")
        if option == 1:
            print("\n" + "-" * 25 + " Adding/Modifying " + "-" * 25)
            element = input("Add the name of the element: ")
            price = int(input("Add the price of the element: "))
            add(element, price)
        elif option == 2:
            print("\n" + "-" * 25 + " Deleting " + "-" * 25)
            element = input("Add the name of the element: ")
            delete(element, products)
        elif option == 3:
            print("You escaped from the program")
            break  # Exit from infinite loop
        else:
            if not option.isdigit():
                print("It is not a digit value! The typed input is not correct!")
            else:
                print("Not correct number! The typed input is not correct!")
        time.sleep(1)


repo(productsDict)


