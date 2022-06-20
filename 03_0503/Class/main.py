import datetime

from feature import Feature     # másik fájlból beimportálunk egy classt


class MainClass:
    def __init__(self):                 #példányosításkor lefutó metódus
        FeatureInstance = Feature()
        FeatureInstance.print_line()

    @staticmethod
    def print_message():                 #static method
        FeatureInstance.print_line()


""""
class MainClass:  # Metódusokat, változókat gyűjtünk bennük - itt nem futtatjuk le, csak létrehozzuk

    line_char: str = "#"                # Class variable

    def print_line(self):
        print(self.line_char * 50)      # Use class variable: self.variable

    # statikus metódus - Nem használnak osztályváltozókat,metódusokat (önállóan vannak, de classon belül)
    # ezeket a metódusokat példányosítás nélkül meg lehet hívni (pl ilyen a time.sleep() is)
    @staticmethod         # dekorátor, leher sajátot is létrehozni
    def print_hello():    # Zárójelek között eltűnt a self
        print("Hello World!")


# Példányosítás - Példánynév nagybetűvel
MainInstance = MainClass()
MainInstance.print_line()       # Felhívjuk a példány függvényét
MainClass.print_hello()         # statikus metódus felhívása példányosítás nélkül
"""





if __name__ == "__main__":                      # ha ez az indító fájl (innen indítjuk a futtatást)
    print("Name of the file: " + __name__)      # ha innen futtatjuk akkor akkor __name__ == __main__
    MainInstance = MainClass()                  # példányosításkor lefutó metódus itt fut le
    print(datetime.datetime.now())
    MainInstance.print_message()