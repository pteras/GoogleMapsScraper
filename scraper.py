import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyB4LyVDfTiPPS6cLQvRGLJMSTEE0Dp3rLs')

address = input('Anna osoitteesi:  \n')
# Address geocoding = osoite -> long ja lat
address_geocode = gmaps.geocode(input)
print(address_geocode)

# kysy osoite
# kysy etäisyys 
# mitä haluaa hakea? esim kahvila, pizza, burger
# laske mikä yritys lähin 
# rajaa vastaukset top 10 (sort by lähin ja kerro etäisyys)
# profit 

