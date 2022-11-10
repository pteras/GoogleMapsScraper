import googlemaps
from math import radians, cos, sin, asin, sqrt
from datetime import datetime
import json
import os

gmaps = googlemaps.Client(key="AIzaSyB4LyVDfTiPPS6cLQvRGLJMSTEE0Dp3rLs")

# Testing geocode
address = 'Joukahaisenkatu 7 Turku'
#address = input('Type in your address: \n')
business = 'restaurant' 
#business = input('What kind of business/restaurant do you want to search: \n')
meters = int(100)
#meters = int(input('Search radius in meters: \n'))

address_longlat = gmaps.geocode(address)[0]
lat1 = address_longlat['geometry']['location']['lat']
lon1 = address_longlat['geometry']['location']['lng']

address_longlat = lat1,lon1
# !!!
places = gmaps.places_nearby(location= address_longlat, type=business, rank_by='distance')

#places = gmaps.places_nearby(location= address_longlat,radius=meters, type=business, rank_by='distance')
# print(json.dumps(places, indent=2))

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

count=1

if places['status'] == 'ZERO_RESULTS':
        print ('No results found with your current parameters.')
else:
    print ('Here are your results: ')

for location in places['results']:
    lat2 = location['geometry']['location']['lat']
    lon2 = location['geometry']['location']['lng']
    business_name = location['name']
    if "rating" in location:
        print(location["rating"])
    else:
        print('No rating found.')
    # if "open" in location:
    #     print(location["open"])
    # rating = location['rating']
    # print(rating)
    # need to round result
    print(str(count)+'.')
    count += 1
    if distance(lat1, lat2, lon1, lon2) >= 1:
        print(r'The distance to', business_name, 'is:',distance(lat1, lat2, lon1, lon2), "kilometers ")
    else: 
        print(r'The distance to', business_name, 'is:',distance(lat1, lat2, lon1, lon2)*1000, "meters")
