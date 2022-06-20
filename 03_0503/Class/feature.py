class Feature:

    line_char: str = "#"

    def print_line(self):
        print(self.line_char * 50)

    @staticmethod           # beépített dekorátor, jelölő
    def print_hello():
        print("Hello World")
        print("Name of the file: " + __name__)  # ha innen van indítva akkor = __name__, ha más fájlból van felhívva ez a metódus: feature


"""if __name__ == "__main__":  # ha ez az indító fájl
    Feature.print_hello()"""

"""MainInstance = Feature()  # példányosítás osztályból - () - végrehajtódik, futtatódik az osztály
MainInstance.print_hello()
Feature.print_line()
Feature.print_hello()"""
