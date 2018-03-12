import xml.etree.ElementTree as ET
import urllib.request as req
from operator import itemgetter
from xml.dom import minidom


def read_from_xml(filename):
    tree = ET.parse(filename)
    return tree.getroot()


def write_cities_to_xml(filename, cities):
    root = ET.Element('cities')
    for city in cities:
        ET.SubElement(root, 'city', name=f"{city['name']}", count=f"{city['count']}")
    with open(filename, "w") as f:
        f.write(minidom.parseString(ET.tostring(root)).toprettyxml(indent='\t'))


cities = []
for city in read_from_xml('data/ua_cities.xml'):
    cities.append({
        "count": 0,
        "name": city.attrib['name']
    })
for site in read_from_xml('data/sites.xml'):
    request = req.Request(site.attrib['url'], headers={'User-Agent': "Magic Browser"})
    response = req.urlopen(request).read().decode('utf-8')
    for index in range(len(cities)):
        cities[index]['count'] += response.count(cities[index]['name'])

new_list = sorted(cities, key=itemgetter('count'), reverse=True)
print(new_list)
write_cities_to_xml('data/out.xml', new_list)
