
import fireapi
import fireapi.config

import zipcodes
import requests

import math

def zipToLatLong(zipc):
    zipcode_data = zipcodes.matching(zipc)[0]
    lat  = zipcode_data['lat']
    long = zipcode_data['long']
    return (lat, long)

def zipToState(zipc):
    zipcode_data = zipcodes.matching(zipc)[0]
    return zipcode_data['state']

def euclideanDistance(lata, longa, latb, longb):
    lata = float(lata)
    latb = float(latb)
    longa = float(longa)
    longb = float(longb)
    dist = math.sqrt((latb - lata)*(latb - lata) + (longb - longa)*(longb - longa))
    return dist

def nearestShelter(zipc):
    shelters = requests.get(fireapi.config.shelter_query).json()["features"]
    # Check in zipcode
    closer = list(filter(lambda x : x["attributes"]["ZIP"] == zipc, shelters))
    if not len(closer) == 0:
        printShelter(closer[0])
    # Check in state
    state = zipToState(zipc)
    closer = list(filter(lambda x : x["attributes"]["STATE"] == state, shelters))
    if not len(closer) == 0:
        (lata, latb) = zipToLatLong(zipc)
        def dist(x):
            x = x["attributes"]
            new_dist = euclideanDistance(lata, x["LATITUDE"], latb, x["LONGITUDE"])
            return new_dist
        closer = sorted(closer, key=dist)
        printShelter(closer[0])

def printShelter(shelter):
    shelter = shelter["attributes"]
    print("Nearest shelter is")
    print("\t{}".format(shelter["SHELTER_NAME"]))
    if "ADDRESS_1" in shelter:
        print("\t{}".format(shelter["ADDRESS_1"]))
    else:
        print("\tWhat sort of database of emergency shelters not have street addresses?")
    print("\t{}, {} {}".format(shelter["CITY"], shelter["STATE"], shelter["ZIP"]))
    # Other info
    print("Other Info")
    if "LATITUDE" in shelter and "LONGITUDE" in shelter:
        print("\tlat:{}\n\tlon:{}".format(shelter["LATITUDE"], shelter["LONGITUDE"]))


