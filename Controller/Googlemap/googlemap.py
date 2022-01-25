import googlemaps
from googlemaps import places
from dotenv import load_dotenv

global gmaps

gmaps=googlemaps.Client(key=f'')

def onSearchMap(keyword):
    place= places.places_autocomplete_query(gmaps,keyword)
    print(place)
    return place
