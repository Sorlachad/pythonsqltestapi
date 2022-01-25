import googlemaps
from googlemaps import places

global gmaps
gmaps=googlemaps.Client(key='AIzaSyC1CU6tWboJLIF-3hagayTt449rdVZTblI')

def onSearchMap(keyword):
    place= places.places_autocomplete_query(gmaps,keyword)
    print(place)
    return place
