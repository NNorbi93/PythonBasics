# Author: NNEMET

"""                           Doc string (as documentation)
Module is not for import
"""


class MainClass:            # Classok functionok csoportosítására, Nagy kezdőbetűvel kezdjük mindent szót
    """
    This class is for practice. CTRL+egérrel ráviszednél kiírja ezt
    """

    class_variable: str = "default value"

    def __init__(self, class_variable: str = "default argument"):  # __init__ always exists,
        # __XYZ : privát, nem lehet kívülről meghívni (nem ajánlja fel a PyCharm)
        # __XYZ__: előre definiált, alapból létezik, ilyenkor csak meghatározzuk a tartalmát
        self.class_variable = class_variable

    def just_a_method(self):
        print(self.class_variable)

    @staticmethod
    def static_thing():     # alulvonást használunk
        """
        this method type will try to reach a class variable without success.
        :param: - paraméterek, argumentumok
        :return: - visszatérési érték
        """

        try:
            print(self.class_variable)
        except Exception as err:
            print(err)

        print("This is a static method. Cannot use class variables")


if __name__ == "__main__":
    instance = MainClass("NonDEF value")
    instance.just_a_method()
    instance.static_thing()
    print("-"*50)
    instance2 = MainClass()
    instance2.just_a_method()
    instance2.static_thing()
