
import zipcodes

def zipToLatLong(zipc):
    zipcode_data = zipcodes.matching(zipc)[0]
    lat  = zipcode_data['lat']
    long = zipcode_data['long']
    return (lat, long)

def zipToState(zipc):
    zipcode_data = zipcodes.matching(zipc)[0]
    return zipcode_data['state']
