import fireapi
import fireapi.config
import fireapi.commands
import sys

zipcode = sys.argv[1]

print(fireapi.commands.zipToLatLong(zipcode))
print(fireapi.commands.zipToState(zipcode))

fireapi.commands.nearestShelter(zipcode)