import datetime
import time
from pprint import pprint

################## Dictionary ##################
def dict_test():
    dict_a_thor = {                 # Create dictionary,  (key-value párok) json-höz hasonló
        "window": 78000,
        "door": 60000,
        "boolean_var" : True,
        "dict": {                   # Dictionary element
            "sub": "asdasd"
        }
    }

    dict_a_thor.pop("door")         # Remove element key (value-val együtt)
    print("#"*50)                   # Separator
    print(dict_a_thor)
    pprint(dict_a_thor)             # Formatted printing (szépen írja ki)
    dict_a_thor["window"] = 80000   # Add or Modify (ha már létezik) - értékadás (listáknál is ezt használjuk)
    print(f"How much is the window: {dict_a_thor.get('window')}") # Get value - get methodus - None-t dob vissza, ha nem létezik, biztonságosabb
    print(f"How much is the window: {dict_a_thor['window']}")       # Get value - Exeption-t dob vissza, ha nem létezik


dict_test()

################## List ##################
# Only values without keys
def list_and_for_cycle():
    test_list = [
        "e1",
        45,
        123.23,
        [               # List element
            "e2",
            "e3"
        ]
    ]

    print(range(5, 10))         # result: range(5, 10) - tól-ig sorozatot, listást legenerál
    print(len(test_list))       # result: 4 - visszaadja a méretét, hosszát, fő elemek számát

    test_list.append("Appended data")   # Add element
    # CTRL + click - jump to source of method

    #test_list.pop()                     # Remove and return item at index (default last)
    #test_list.remove()                  # Remove first occurrence of value.

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

################## Loops ##################
def while_true():  # Infinite loop
    while True:
        timestamp = datetime.datetime.now()
        print(timestamp)

        time.sleep(1)
        if ":01" in str(timestamp):
            break  # Exit from infinite loop (belső ciklusból lép ki)
    return # egész functionból kilép

# continue - újra kezdjük a ciklust (visszaugrik a ciklus elejére)

while_true()
