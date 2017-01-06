# a script to show some of the interfaces we can use
# last modified: January 5, 2017

import googlemaps

key = raw_input('Input API key: ')
client = googlemaps.Client(key)

# get directions from one location to another

start = "15 Orchard Road Newark, DE 19716"
destination = "1901 N Dupont Hwy, New Castle, DE 19720"

routes = client.directions(start,destination,mode="driving",avoid="tolls",
                           units="metric",region="us")

for j in range(len(routes[0]['legs'][0]['steps'])):
    print routes[0]['legs'][0]['steps'][j]['html_instructions']
