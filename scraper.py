import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyB4LyVDfTiPPS6cLQvRGLJMSTEE0Dp3rLs")

# Testing geocode #
address_geocode = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(address_geocode)

