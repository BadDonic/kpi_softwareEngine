from cities import *

path = 'resources/'

if __name__ == '__main__':
    cities = read_cities_xml(path + 'ua_cities.xml')
    sites = get_data_sites(path + 'sites.xml')
    write_cities_xml(path + "out.xml", count(cities, sites))
