import datetime
import time
from pprint import pprint

################## Dictionary ##################
# Nincs sorrend
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
print("-"*50)

################## List ##################
# Only values without keys
# Van sorrend

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

    print(range(5, 10))         # result: range(5, 10) - tól-ig sorozatot, listát legenerál
    # kezdő és végérték, harmadik a lépésnagyság lenne
    # printelve nem lista formájú, mint sima string lesz kiiratva (OOP-vel kapcsoaltos a magyarázata)

    test_list.append("Appended data")   # Add element
    # CTRL + click - jump to source of method

    print(f"Lenght of list: {len(test_list)}")  # result: 5 - visszaadja a méretét, hosszát, fő elemek számát

    #test_list.pop()                     # Remove and return item at index (default last)
    #test_list.remove()                  # Remove first occurrence of value.

################## FOR ##################
    for index in range(len(test_list)):         # = range(5) Range of length of list = 0, 1, 2, 3, 4
        # index: local variable (csak cikluson belül érvényes), ideiglenes counter
        print(f"{index}: {test_list[index]}")   # Get of value of element (there is no GET method)
        # Print the elements of list

    print("-" * 50)

    #print("\n")                                  # \n - new line
    for index, element in enumerate(test_list):  # enumerate: végigjárja a listát
        # gives you back two loop variables: index and element
        if type(element) == list:               # Type of variable
            print(f"This is a list:")
            for i, e in enumerate(element):     # adatott elemet körbejárjuk
                print(f"\t{i}: {e}")            # \t - tabulator
        else:
            print(f"{index} - {element}")

# Alt + J - select the next occurance

list_and_for_cycle()
print("-"*50)

################## WHILE ##################
def while_true():  # Infinite loop
    while True:    # amíg igaz ... - itt nincs feltétel
        timestamp = datetime.datetime.now()
        print(timestamp)                    # print egyből megpróbálja stringgé alakítani
        # continue - újra kezdjük a ciklust, ami mögötte van azt nem futtatja le(visszaugrik a ciklus elejére)
        time.sleep(1)   # hány másodpercet várson
        # string keresése stringben
        if "95" in str(timestamp):  # stringgé kell alakítani hogy iterálható legyen, mert a datetime nem string hanem komplex adattipus
            break                   # Exit from infinite loop (belső ciklusból lép ki)
    return                          # egész functionból kilép visszatérési érték nélkül

while_true()

"9"     # stringgé alakító operáció - nem lehet exeption handlinget alkalmazni
str(9)  #metódus - lehet exeption handlinget alkalmazni ezért ezt preferáljuk inkább

