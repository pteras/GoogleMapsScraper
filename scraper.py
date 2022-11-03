import googlemaps
from math import radians, cos, sin, asin, sqrt
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyB4LyVDfTiPPS6cLQvRGLJMSTEE0Dp3rLs")

# Testing geocode
address_geocode = gmaps.geocode('Ruukinrinne 4, Turku, Finland')
print(address_geocode)

print(gmaps.find_place("restaurant", "textquery",location_bias="circle:1000@60.45519009999999,22.3045487",language="fi"))
# Get location 


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
     
     
# driver code
lat1 = 60.45519009999999
lon1 = 22.3045487
lat2 = 60.45715565610971
lon2 =  22.29241985762579
print(distance(lat1, lat2, lon1, lon2), "km")
# jos alle km ni muuta metreiksi


