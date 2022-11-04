import googlemaps
from math import radians, cos, sin, asin, sqrt
from datetime import datetime
import json
import os

gmaps = googlemaps.Client(key="AIzaSyB4LyVDfTiPPS6cLQvRGLJMSTEE0Dp3rLs")

# Testing geocode
#address = 'Ruukinrinne 4 Turku'
address = input('Type in your address: \n')
business = input('What kind of business/restaurant do you want to search: \n')
meters = int(input('Search radius in meters: \n'))

address_longlat = gmaps.geocode(address)[0]
#print(address_longlat)
#address_longlat.keys()
lat1 = address_longlat['geometry']['location']['lat']
lon1 = address_longlat['geometry']['location']['lng']

#print(lat1)
#print(lon1)

address_longlat = lat1,lon1
# !!!
places = gmaps.places_nearby(location=address_longlat,radius=meters, type=business)
print(json.dumps(places, indent=2))

# Calculate Distance Between Two Points on Earth
def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)
       
# driver code for distance
# need to get places longs and lats !!! 

lat2 = 60.45715565610971
lon2 =  22.29241985762579

# need to round results
if distance(lat1, lat2, lon1, lon2) >= 1:
    print(distance(lat1, lat2, lon1, lon2), "km")
else: 
    print(distance(lat1, lat2, lon1, lon2)*1000, "m")


#paikka = gmaps.find_place("restaurant", "textquery",location_bias="circle:10@60.45519009999999,22.3045487")
#print(paikka)
#print(gmaps.reverse_geocode(paikka["candidates"][0]["place_id"]))