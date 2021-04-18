import zipcodes
import requests

def zipToLatLong(zipc):
    zipcode_data = zipcodes.matching(zipc)[0]
    lat  = zipcode_data['lat']
    long = zipcode_data['long']
#    return (lat, long)

    url = "https://api.ambeedata.com/latest/fire"
#    querystring = {'lat': "45.5544", 'lng': "-122.8113"}
    int arr[2]
    arr[0] = lat
    arr[1] = long
    headers = {'x-api-key': "Tpt2eNLB5k5aVxjScKbvt1F9v7oSjgFc4CPWPITQ", 'Content-type': "application/json"}
    response = requests.request("GET", url, headers=headers, params=arr)
    print(response.text)

