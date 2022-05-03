import json


class DataHandling:

    data: dict = {}
    text: str = ""

    def __init__(self):
        pass

    def read_json(self):
        with open(file="data.json", mode="r", encoding="utf-8") as json_file:  # bezárja a fájlt a végén
            self.data = json.load(json_file)  # dict-é formázza
        print(self.data)

    def write_json(self):
        with open(file="data.json", mode="w", encoding="utf-8") as json_file: # teljesen újraírja 0ról (hozzáírás ="w+")
            json.dump(self.data, json_file)


MainInstance = DataHandling()
MainInstance.read_json()
