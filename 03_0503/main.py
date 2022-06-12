import datetime

from feature import Feature


class MainClass:

    def __init__(self):  # példányosításkor lefutó metódus
        FeatureInstance = Feature()
        FeatureInstance.print_line()

    @staticmethod
    def print_message():
        Feature.print_hello()


if __name__ == "__main__":  # ha ez az indító fájl (innen indítjuk a futtatást)
    print("Name of the file: " + __name__)        # ha innen futtatjuk akkor akkor __name__ == __main__
    MainInstance = MainClass() # példányosításkor lefutó metódus itt fut le
    print(datetime.datetime.now())
    MainInstance.print_message()