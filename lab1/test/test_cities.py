import unittest
from cities import *
import json

path = "/home/daniel/Programming/kpi_softwareEngine/lab1/resources/"


class TestCities(unittest.TestCase):
    def test_read_cities_xml(self):
        with open(path + "expect_cities.json", "r") as f:
            cities_list = json.load(f)
        self.assertRaises(FileNotFoundError, read_cities_xml, path + "test")
        self.assertRaises(IsADirectoryError, read_cities_xml, path)
        self.assertRaises(IsADirectoryError, read_cities_xml, path)
        self.assertEqual(cities_list, read_cities_xml(path + "ua_cities.xml"))

    def test_write_cities_xml(self):
        cities_list = [{'count': 0, 'name': 'Киев'}, {'count': 0, 'name': 'Старобельск'}]
        self.assertRaises(IsADirectoryError, write_cities_xml, path, [])
        write_cities_xml(path + "out.xml", [])
        self.assertEqual([], read_cities_xml(path + "out.xml"))
        write_cities_xml(path + "out.xml", cities_list)
        self.assertEqual(cities_list, read_cities_xml(path + "out.xml"))

    def test_count(self):
        site_data = []
        cities_list = [
            {'count': 0, 'name': 'Киев'}, {'count': 0, 'name': 'Старобельск'}, {'count': 0, 'name': 'Луганск'},
            {'count': 0, 'name': 'Днепропетровск'}, {'count': 0, 'name': 'Лисичанск'}, {'count': 0, 'name': 'Луцк'},
            {'count': 0, 'name': 'Ровно'}, {'count': 0, 'name': 'Никополь'}, {'count': 0, 'name': 'Берегово'},
            {'count': 0, 'name': 'Львов'}, {'count': 0, 'name': 'Болград'}, {'count': 0, 'name': 'Харьков'},
            {'count': 0, 'name': 'Херсон'}
        ]
        expect_cities = [
            {'count': 12, 'name': 'Киев'}, {'count': 8, 'name': 'Старобельск'}, {'count': 6, 'name': 'Луганск'},
            {'count': 5, 'name': 'Днепропетровск'}, {'count': 5, 'name': 'Лисичанск'}, {'count': 4, 'name': 'Луцк'},
            {'count': 4, 'name': 'Ровно'}, {'count': 2, 'name': 'Никополь'}, {'count': 1, 'name': 'Берегово'},
            {'count': 1, 'name': 'Львов'}, {'count': 1, 'name': 'Болград'}, {'count': 1, 'name': 'Харьков'},
            {'count': 1, 'name': 'Херсон'}
        ]

        with open(path + "test_site.json", "r") as f:
            site_data.append(json.load(f))

        self.assertEqual([], count([], []))
        self.assertEqual(cities_list, count(cities_list, []))
        self.assertEqual([], count([], site_data))
        self.assertEqual(expect_cities, count(cities_list, site_data))


if __name__ == '__main__':
    unittest.main()
