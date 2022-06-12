import unittest
import pytest

from unittest_gyak.main import ToBeTested  # fájl beimportálása amit tesztelni akarunk

class TestStringMethods(unittest.TestCase):  # Örököl a unittest modul TestCase classától
    def setUP(selfs) -> None:     # Minden teszt előtt meg lesz hívva, de nem csinál semmit
        print("Start the test...\n you can setup logging, network stack, etc. in setUp()")


