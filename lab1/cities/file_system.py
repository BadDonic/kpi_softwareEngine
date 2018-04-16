from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, parse, tostring


def read_xml(filename):
    tree = parse(filename)
    return tree.getroot()


def write_cities_xml(filename, cities):
    root = Element('cities')
    for city in cities:
        SubElement(root, 'city', name=f"{city['name']}", count=f"{city['count']}")
    with open(filename, "w") as f:
        f.write(minidom.parseString(tostring(root)).toprettyxml(indent='\t'))


def read_cities_xml(filename):
    cities = []
    for city in read_xml(filename):
        cities.append({
            "count": 0,
            "name": city.attrib['name']
        })
    return cities
