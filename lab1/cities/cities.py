from operator import itemgetter
from .file_system import read_xml
import feedparser


def get_data_sites(filename):
    sites = []
    for site in read_xml(filename):
        sites.append(feedparser.parse(site.attrib['url']))
    return sites


def count(cities, sites_data):
    for site in sites_data:
        for index in range(len(cities)):
            cities[index]['count'] += str(site).count(cities[index]['name'])
    return sorted(cities, key=itemgetter('count'), reverse=True)
