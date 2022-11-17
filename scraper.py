import googlemaps
from math import radians, cos, sin, asin, sqrt
import json

gmaps = googlemaps.Client(key="AIzaSyB4LyVDfTiPPS6cLQvRGLJMSTEE0Dp3rLs")

# comments for testing
# address = 'Joukahaisenkatu 7 Turku'
address = input('Type in your address: \n')
# business_input = 'moving company'
business_input = input('What kind of business/restaurant do you want to search: \n')
business = business_input.replace(' ', '_')
# radius_km = int(5000)/1000
radius = int(input('Search radius in meters: \n'))
radius_km = radius/1000

# address into latitude and longitude values
address_longlat = gmaps.geocode(address)[0]
lat1 = address_longlat['geometry']['location']['lat']
lon1 = address_longlat['geometry']['location']['lng']

address_longlat = lat1,lon1
# returns places nearby
places = gmaps.places_nearby(location= address_longlat, type=business, rank_by='distance')
# print(json.dumps(places, indent=2))

# with open('json_data.json', 'w') as outfile:
# json.dump(places, outfile)

# calculates distance between two locations
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
    
    # radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return round(c * r,3)
       
# driver code

count=1
print('We are looking for a',business_input,'within',radius,'meters \n')

if places['status'] == 'ZERO_RESULTS':
        print ('No results found with your current parameters.')
else:
    print ('Here are your results: \n')

for location in places['results']:
    lat2 = location['geometry']['location']['lat']
    lon2 = location['geometry']['location']['lng']
    business_name = location['name']

    if distance(lat1, lat2, lon1, lon2) <= radius_km:
        print(str(count)+'.')
        if distance(lat1, lat2, lon1, lon2) >= 1:
            print(r'The distance to', business_name, 'is:',distance(lat1, lat2, lon1, lon2), "kilometers ")
        else: 
            print(r'The distance to', business_name, 'is:',distance(lat1, lat2, lon1, lon2)*1000, "meters")
        if "rating" in location:
            print(r'Rating:',location["rating"])
        else:
            print('No ratings.')
        # Tässä pieni ongelma
        if "open_now" == True:
            print('Status: Open') 
        else: 
            print('Status: Closed')

        print('Address:',location['vicinity'],'\n')

        count += 1
