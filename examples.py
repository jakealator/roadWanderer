# a script to show some of the interfaces we can use
# last modified: January 6, 2017

import googlemaps
from pygeocoder import Geocoder

key = raw_input('Input API key: ')
client = googlemaps.Client(key)

# get directions from one location to another

start = "15 Orchard Road Newark, DE 19716"
destination = "1901 N Dupont Hwy, New Castle, DE 19720"

routes = client.directions(start,destination,mode="driving",avoid="tolls",
                           units="metric",region="us")

for j in range(len(routes[0]['legs'][0]['steps'])):
    print routes[0]['legs'][0]['steps'][j]['html_instructions']

# find something nearby
location = "15 Orchard Road Newark, DE 19716"
location = Geocoder.geocode(location).coordinates

interest = raw_input("what are you looking for? ")
interest = interest.replace(" ","_")  #I think we need underscores
language = "en_US" #MAGA
dist = 50 #miles?

options = client.places('restaurant',location=location,type=interest,language=language,
                        min_price=1,max_price=4,open_now=True,radius=dist)

for j in range(len(options['results'])):
    print options['results'][j]['name']



