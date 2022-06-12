# Author: NNEMET

"""                             # Doc string (as documentation)
Module is not for import
"""


class MainClass:            # Classok functionok csoportosítására
    """
    This class is for practice.
    """

    class_variable: str = "default value"

    def __init__(self, class_variable: str = "default argument"):  # __init__ always exists
        print(self.class_variable)

    @staticmethod
    def static_thing():
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
