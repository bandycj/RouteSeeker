import json
from lxml.cssselect import CSSSelector
import os
import urllib2
import re
from lxml.html import parse
from local_settings import MAPQUEST_TOKEN

__author__ = 'e83800'

AIRPORT_URL = "http://www.southwest.com/html/air/airport-information.html"

CITY_ROWS = CSSSelector('td.city')
STATION_ID_DIV = CSSSelector('div.stationID')
AIRPORT_NAME_DIV = CSSSelector('div.airport_name')

def nearest_airport(lat, lng):
    url = "http://www.mapquestapi.com/search/v1/radius?mapData=nadb,1547&radius=50.0&key=" + MAPQUEST_TOKEN + "&origin=" + lat + "," + lng
    airports = get_airports()
    output = json.load(urllib2.urlopen(url))
    if 'searchResults' in output:
        for result in output['searchResults']:
            found = None
            for airport in airports:
                iataCode = airport.iataCode
                regex = re.compile(r'.*((?:%s;)|(?:%s$))' % (iataCode, iataCode), re.IGNORECASE)
                if regex.search(result[u'name']) is not None:
                    found = airport
                    break
            if found is not None:
                print "%s : %s" % (found, result[u'name'])
                break

def get_timezones():
    timezones = {}
    airportsDat = os.path.join(os.getcwd(),"./utils/airports.dat")
    import csv
    with open(airportsDat, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            iataCode = row[4].decode('utf-8')
            offset = row[9].decode('utf-8')
            dst = row[10].decode('utf-8')
            timezones[iataCode]={
                'offset': offset,
                'dst': dst
            }

    return timezones

def get_airports():
    doc = parse(AIRPORT_URL).getroot()
    timezones = get_timezones()
    return_list = []
    for row in CITY_ROWS(doc):
        iataCode=STATION_ID_DIV(row)[0].text
        return_list.append({
            'iataCode':iataCode,
            'name': AIRPORT_NAME_DIV(row)[0].text,
            'tz_offset':timezones[iataCode]['offset'],
            'dst':(timezones[iataCode]['dst'] == 'A')
        })
    return return_list