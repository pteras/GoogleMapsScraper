import googlemaps
from math import radians, cos, sin, asin, sqrt
import json
from decouple import config

gmaps = googlemaps.Client(key = config('GMAPS_KEY'))

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

def get_data(address, business_type, radius):   
    
    # DOCS: https://googlemaps.github.io/google-maps-services-python/docs/
     
    
    business_type = business_type.replace(' ', '_')        

    radius_km = int(radius)/1000


    # address into latitude and longitude values    
    lat1 = gmaps.geocode(address)[0]['geometry']['location']['lat']
    lon1 = gmaps.geocode(address)[0]['geometry']['location']['lng']
        

    # returns places nearby
    places = gmaps.places_nearby(location= [lat1,lon1], type=business_type, rank_by='distance')       

    if places['status'] == 'ZERO_RESULTS':
            return json.dumps({"success": False, "message": "No results found"}), 200, {"ContentType": "application/json"}
    data = []
    for location in places['results']:
        # print(location)
        data_entry = {}
        lat2 = location['geometry']['location']['lat']
        lon2 = location['geometry']['location']['lng']
        data_entry['name'] = location['name']        

        # calculate distance between two locations
        dist = distance(lat1, lat2, lon1, lon2)
        # if distance is more than radius, continue
        if dist >= radius_km:
            continue
        
        dist_dict = {}
        data_entry['distance'] = dist_dict

        if dist <= 1:
            dist_dict['value'] = dist * 1000
            dist_dict['unit'] = 'm'
                        
        else:        
            dist_dict['value'] = round(dist, 1)
            dist_dict['unit'] = 'km'            
        
        data_entry['rating'] = location['rating'] if "rating" in location else "No rating"        
        data_entry['open_now'] = location['opening_hours']['open_now'] if "opening_hours" in location else "No data"

        data_entry['address'] = location['vicinity']

        data.append(data_entry)        

    return data

  

