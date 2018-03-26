import unittest
from cities import *


class TestCities(unittest.TestCase):
    def test_read_xml(self):
        print(read_xml('../data/ua_cities.xml'))
