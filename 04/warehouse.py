import datetime
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # aktuális fájl (ahonnan futtatunk) útvonala
os.path.join(ROOT_DIR, "modules/data.json")  # path összefűzése

print(str(datetime.datetime.now()))
values: list = ["név", "hozzáadás", {"ablak": 90000}]

values.append("vmi")
values.append("")

print({str(datetime.datetime.now()) : values}) # dictionerybe mint key

# EXCEPTION - számít a sorrend, mindig a legszűkebbe kezdjük, végére tágabb hibacsoport

try:
    input_value: int = int(input("Adj meg egy számtok: "))
    print(input_value)
except TypeError as err:
    print(f"TYPE ERROR: {err}")
except ValueError as err:
    print(f"VALUE ERROR: {err}")
except Exception as err:
    print(f"Exception: {err}")

name: str = "Német Norbert"

if " " in name:
    print("Ne rakjál szóközt")
    name = name.replace(" ", "-")
    name = name.lower()
    print(name.capitalize())