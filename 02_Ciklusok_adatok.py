import datetime
from pprint import pprint
import time


def dict_test():
    dict_a_thor = {                 # Create dictionary
        "window": 78000,
        "door": 60000,
        "Boolean_var": {
            "sub": "asdasd"
        }
    }

    dict_a_thor.pop("door")         # Remove element
    print("#"*50)
    print(dict_a_thor)
    pprint(dict_a_thor)             # Formatted printing
    dict_a_thor["window"] = 80000                                   # Modify
    print(f"How much is the window: {dict_a_thor.get('window')}")   # Get value
    print(f"How much is the window: {dict_a_thor['window']}")       # Get value


dict_test()


def list_and_for_cycle():
    test_list = [
        "e1",
        45,
        123.23,
        [
            "e2",
            "e3"
        ]
    ]

    print(range(5, 10))         # result: range(5, 10)
    print(len(test_list))       # result: 4

    test_list.append("Appended data")   # Add element
    #test_list.pop()                     # Remove element
    #test_list.remove()                  # Remove element

    for index in range(len(test_list)):         # Range of length of list, index: local variable, counter
        print(f"{index}: {test_list[index]}")   # Print the elements of list

    print("\n")                                  # \n - new line
    for index, element in enumerate(test_list):  # enumerate: gives you back two loop variables: index and element
        if type(element) == list:
            print(f"This is a list:")
            for i, e in enumerate(element):
                print(f"\t{i}: {e}")            # \t - tabulator
            print("-"*50)
        print(f"{index} - {element}")


list_and_for_cycle()


def while_true():  # Infinite loop
    while True:
        timestamp = datetime.datetime.now()
        print(timestamp)

        time.sleep(1)
        if ":01" in str(timestamp):
            break  # Exit from infinite loop
    return


while_true()
