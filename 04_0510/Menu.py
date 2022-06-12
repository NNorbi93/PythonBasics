class Menu:

    var1: str = "JAJA"  # osztályváltozó

    def __init__(self):
        pass

    def inheritance_method(self):
        print(self.var1)    # osztályváltozó használata


    @staticmethod
    def menu():
        while True:
            print("")